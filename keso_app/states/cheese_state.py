import io
import csv
import logging
from typing import Optional, Any, TypeVar, Type

import reflex as rx
from pydantic import ValidationError, BaseModel
from supabase import Client

from keso_app.models.tables import CheeseProductionView
from keso_app.states.db_client import get_db_client
from keso_app.constants.shared import NO_FILTER_VALUE, MAX_SEARCH_LENGTH
from keso_app.constants.cheese import CHEESE_CONSTANTS

ModelType = TypeVar('ModelType', bound=BaseModel)

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(funcName)s | %(message)s')

# TODO: add a remove_all_filters method

class CheeseState(rx.State):
    """Manages the state for the cheese production CRUD interface."""

    # --- Data state ---
    data_config = CHEESE_CONSTANTS
    current_page_data: list[dict] = []
    visible_columns: list[tuple[str, str]] = data_config.visible_columns
    sortable_columns: list[tuple[str, str]] = data_config.sortable_columns
    searchable_columns: list[str] = data_config.searchable_columns
    filters_for_ui: list[tuple[str, list[tuple[str, str]]]] = data_config.filters_for_ui
    default_sort_column: str = data_config.default_sort_column
    
    # --- Modal state ---
    selected_cheese: Optional[CheeseProductionView] = None
    show_modal: bool = False
    
    # --- Filter state ---
    # Search
    search_query: str = ""
    # Sort
    column_sorted: str = data_config.default_sort_column
    is_sort_ascending: bool = False
    # Category Filter
    selected_cheese_type: str = "NA"
    active_category_filters: dict[str, str] = {} # key: column name, value: selected value

    # Pagination State
    current_page: int = 1
    total_pages: int = 1
    items_per_page: int = 10

    # Loading state
    is_loading: bool = True

    # --- Helpers ---
    def _build_base_query(
        self, 
        client: Client, 
        select_columns: str = "*", 
        count: Optional[str] = None
    ):
        """Builds the base Supabase query object with filtering and sorting."""
        
        query = client.table(self.data_config.table_name).select(select_columns, count=count)

        # Apply search filtering
        if self.search_query:
            search_term = f"%{self.search_query}%"
            or_conditions = ",".join([
                f"{col}.ilike.{search_term}" for col in self.searchable_columns
            ])
            query = query.or_(or_conditions)

        # Apply category filtering
        if self.active_category_filters:
            for column, value in self.active_category_filters.items():
                query = query.eq(column, value)

        # Apply sorting
        valid_values = [col[0] for col in self.sortable_columns]
        if self.column_sorted in valid_values:
             query = query.order(
                 self.column_sorted, desc=not self.is_sort_ascending
             )

        return query

    async def _execute_query(
        self, 
        paginate: bool = False, 
        fetch_count: bool = False
    ) -> Optional[Any]: # TODO: improve type hinting for response
        """
        Connects to database, builds the query, optionally applies 
        pagination and count, executes, and returns the raw response.

        Args:
            paginate: If True, apply LIMIT/OFFSET based on state.
            fetch_count: If True, add count="exact" to the select.

        Returns:
            The raw response object from Supabase query execution, or None on client error.
        """
        client = get_db_client()
        if not client:
            return None

        try:
            query = self._build_base_query(
                client,
                select_columns="*",
                count="exact" if fetch_count else None
            )

            if paginate:
                limit = self.items_per_page
                offset = self.pagination_offset
                query = query.range(offset, offset + limit - 1)

            logging.info(f"Executing query...")
            response = query.execute()
            logging.info(f"Query successful.")
            return response

        # TODO: Handle specific exceptions from Supabase client
        except Exception as e:
            logging.error(f"Exception during query execution: {e}", exc_info=True)
            raise e

    def _validate_data(
        self,
        raw_items: list[dict[str, Any]],
        data_model: Type[ModelType]
    ) -> tuple[list[ModelType], int]:
        """
        Validates raw data against the provided Pydantic model.

        Args:
            raw_items: List of dictionaries from the database.
            data_model: The Pydantic model class to validate against.

        Returns:
            Tuple: (List of validated model objects, count of validation failures).
        """
        valid_data: list[ModelType] = []
        invalid_count: int = 0
        if not raw_items:
            return valid_data, invalid_count

        model_name = data_model.__name__
        for i, item in enumerate(raw_items):
            try:
                validated_obj = data_model.model_validate(item)
                valid_data.append(validated_obj)
            except ValidationError as e:
                invalid_count += 1
                logging.warning(f"({model_name}) | Item {i+1} Validation failed: {e.errors()} \nRaw Data: {item}")
            except Exception as e:
                invalid_count += 1
                logging.warning(f"({model_name}) | Item {i+1} Skipped due to unexpected error: {e} \nRaw Data: {item}")

        return valid_data, invalid_count


    # --- Core Data Fetching ---
    @rx.event(background=True)
    async def fetch_data(self):
        """Fetches paginated data, validates and updates state."""

        processed_data: list[ModelType] = []
        invalid_count: int = 0
        total_db_count: int = 0
        events_to_yield = []

        async with self:
            self.is_loading = True

        try:
            response = await self._execute_query(paginate=True, fetch_count=True) 

            if response is None:
                 yield rx.toast.error("Fetch failed: Database unavailable.", duration=4000)
                 return

            raw_items = response.data or []
            total_db_count = response.count or 0

            processed_data, invalid_count = self._validate_data(raw_items, CheeseProductionView)

            async with self:
                self.current_page_data = [item.model_dump() for item in processed_data] # TODO: try to send original model
                self.total_pages = (total_db_count + self.items_per_page - 1) // self.items_per_page
                if self.total_pages == 0: self.total_pages = 1
                logging.info(f"State updated. Displaying: {len(self.current_page_data)}, Total Pages: {self.total_pages}")

            if invalid_count > 0:
                if invalid_count == len(raw_items) and len(raw_items) > 0:
                     events_to_yield.append(rx.toast.error(f"All {invalid_count} rows on this page are invalid.", duration=5000))
                else:
                    events_to_yield.append(rx.toast.warning(f"{invalid_count} row(s) skipped due to data errors.", duration=5000))

        except Exception as e:
            logging.error(f"Exception during fetch_data: {e}", exc_info=True)
            events_to_yield.append(rx.toast.error("Failed to fetch data.", duration=4000))
            async with self:
                self.current_page_data = []
                self.total_pages = 1
        finally:
            async with self:
                self.is_loading = False
            for event in events_to_yield:
                yield event

    @rx.event(background=True)
    async def download_csv(self):
        """Generates and downloads a CSV of VALID filtered/sorted data."""

        validated_data: list[ModelType] = []
        invalid_count: int = 0
        events_to_yield = []

        try:
            response = await self._execute_query(paginate=False, fetch_count=False)

            if response is None:
                yield rx.toast.error("Download failed: Database unavailable.", duration=4000)
                return

            raw_items = response.data or []
            validated_data, invalid_count = self._validate_data(raw_items, CheeseProductionView)

            output = io.StringIO()
            headers = list(CheeseProductionView.model_fields.keys())
            writer = csv.DictWriter(output, fieldnames=headers, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()

            if not validated_data:
                if raw_items:
                     events_to_yield.append(rx.toast.error(f"Download failed: All {len(raw_items)} rows were invalid.", duration=5000))
                else:
                     events_to_yield.append(rx.toast.info("No data found matching criteria.", duration=4000))
            else:
                for valid_obj in validated_data:
                    writer.writerow(valid_obj.model_dump())

                if invalid_count > 0:
                    events_to_yield.append(rx.toast.warning(f"{invalid_count} row(s) were skipped due to errors.", duration=5000))
                events_to_yield.append(rx.toast.success("CSV generated successfully.", duration=3000))

            # --- Finalize CSV and Yield Download ---
            csv_data = output.getvalue()
            output.close()
            if not (raw_items and not validated_data):
                filename = "cheese_data_export_validated.csv" if validated_data else "cheese_data_export_empty.csv"
                events_to_yield.append(rx.download(data=csv_data, filename=filename))

        except Exception as e:
            logging.error(f"Exception during CSV generation: {e}", exc_info=True)
            events_to_yield.append(rx.toast.error("Failed to generate CSV.", duration=4000))
        finally:
            if 'output' in locals() and not output.closed: output.close()
            for event in events_to_yield:
                yield event

    async def set_items_per_page(self, items: str):
        """Updates items per page, resets pagination, and fetches data."""

        original_items_per_page = self.items_per_page
        try:
            items = int(items)
            if items < 1:
                items = 1
            self.items_per_page = items
        except ValueError:
            self.items_per_page = 10

        if self.items_per_page != original_items_per_page:
            self.current_page = 1
            yield CheeseState.fetch_data()


    # UI Control Handlers
    
    # Sorting
    async def toggle_sort_direction(self):
        """Toggles the sort direction (ASC/DESC)."""
        self.is_sort_ascending = not self.is_sort_ascending
        self.current_page = 1
        yield CheeseState.fetch_data()
    
    async def handle_sort_column(self, column: str):
        """Sets the column to sort by, from the dropdown."""
        
        valid_values = [col[0] for col in self.sortable_columns]
        if column not in valid_values:
            logging.error(f"Invalid column: {column}")
            return
        if self.column_sorted == column:
            logging.error(f"Same column: {column}")
            return

        self.column_sorted = column
        self.is_sort_ascending = False
        self.current_page
        yield CheeseState.fetch_data()
    
    # Filtering
    async def handle_search_query(self, query: str):
        """Updates the search query after sanitization and fetches data."""

        sanitized_query = query.strip()

        if len(sanitized_query) > MAX_SEARCH_LENGTH:
            sanitized_query = sanitized_query[:MAX_SEARCH_LENGTH]
            yield rx.toast.info("Search query was too long and has been truncated.", duration=3000)

        if self.search_query == sanitized_query:
             return

        self.search_query = sanitized_query
        self.current_page = 1
        yield CheeseState.fetch_data()
    
    async def handle_category_filter(self, column_to_filter: str, selected_value: str):
        """
        Updates the active_category_filters attribute based on user's input.

        Args:
            column_to_filter: The column name to filter on.
            selected_value: The value selected to filter on.
        """
        if not any(column == column_to_filter for column, _ in self.filters_for_ui):
            return

        filters_changed: bool = False
        current_filter_value = self.active_category_filters.get(column_to_filter)

        if selected_value == NO_FILTER_VALUE: # TODO: consider removing filter if the same value is selected
            if column_to_filter in self.active_category_filters:
                del self.active_category_filters[column_to_filter]
                filters_changed = True
        else:
            if current_filter_value != selected_value:
                self.active_category_filters[column_to_filter] = selected_value
                filters_changed = True

        if filters_changed:
            self.current_page = 1
            yield CheeseState.fetch_data()
    
    
    # Pagination
    @rx.var
    def pagination_offset(self) -> int:
        """Calculates the offset for Supabase pagination. Safe computed var."""
        return (self.current_page - 1) * self.items_per_page
    
    async def go_to_next_page(self):
        """Goes to the next page if possible and fetches data."""
        if self.current_page < self.total_pages:
            self.current_page += 1
            yield CheeseState.fetch_data()

    async def go_to_prev_page(self):
        """Goes to the previous page if possible and fetches data."""
        if self.current_page > 1:
            self.current_page -= 1
            yield CheeseState.fetch_data()

    async def go_to_first_page(self):
        """Goes to the first page if not already there."""
        if self.current_page > 1:
            self.current_page = 1
            yield CheeseState.fetch_data()

    async def go_to_last_page(self):
        """Goes to the last page if not already there."""
        if self.current_page < self.total_pages:
            self.current_page = self.total_pages
            yield CheeseState.fetch_data()

    # Modal handling
    def toggle_modal(self):
        self.show_modal = not self.show_modal
        if not self.show_modal:
            self.selected_cheese = None

    def select_db_entry(self, db_entry: dict[str, Any]):
        
        valid_data: ModelType
        try:
            valid_data = CheeseProductionView.model_validate(db_entry)
        except ValidationError as e:
            rx.toast.error(f"Validation failed.")
            logging.error(f"Validation error: {e}")
            return
        except Exception as e:
            rx.toast.error("Unexpected error. Check terminal for details.")
            logging.error(f"Unexpected error: {e}")
            return
        
        self.selected_cheese = valid_data
        return CheeseState.toggle_modal

