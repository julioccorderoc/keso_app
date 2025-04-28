import reflex as rx

# Constant to represent that no filter is applied
NO_FILTER_LABEL = "All"
NO_FILTER_VALUE = "NA"

# Lenght of the search queries
MAX_SEARCH_LENGTH = 100

class ColumnConfig(rx.Base):
    """Represents a single column configuration."""
    label: str
    tag: str
    default_sort: bool
    visible: bool
    sortable: bool
    filterable: bool
    searchable: bool
    filter_options: dict[str, str] | None

class TableConstants(rx.Base):
    """Base class for table constants."""

    table_name: str
    column_config: dict[str, ColumnConfig]
    
    @property
    def visible_columns(self) -> list[tuple[str, str]]:
        """Get a list of visible column names."""
        columns: list[tuple[str, str]] = [
            (col_name, config.label) 
            for col_name, config in self.column_config.items() 
            if config.visible
        ]
        return columns
    
    @property
    def sortable_columns(self) -> list[tuple[str, str]]:
        """Get a list of sortable column names."""
        columns: list[tuple[str, str]] = [
            (col_name, config.tag) 
            for col_name, config in self.column_config.items() 
            if config.sortable
        ]
        return columns

    @property
    def searchable_columns(self) -> list[str]:
        """Get a list of searchable column names."""
        columns: list[str] = [
            col_name 
            for col_name, config in self.column_config.items() 
            if config.searchable
        ]
        return columns

    @property
    def filters_for_ui(self) -> dict[str, dict[str, str]]:
        """
        Get a dictionary of filters for UI generation.
        Key: column name, Value: {label:value}
        """
        filters: dict[str, dict[str, str]] = {
            col_enum: config.filter_options
            for col_enum, config in self.column_config.items()
            if config.filterable and config.filter_options is not None
        }
        return filters
    
    @property
    def default_sort_column(self) -> str:
        """Get the default sort column name."""
        column_name: str = next(
            (col_enum for col_enum, config in self.column_config.items() if config.default_sort),
            # Fallback to the first sortable column if none marked as default
            next((col_enum for col_enum, config in self.column_config.items() if config.sortable), None)
        )
        return column_name
