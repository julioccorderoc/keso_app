# app.py
import reflex as rx
import datetime
import calendar
from typing import List, Tuple, Optional

# Constants
WEEKDAYS = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

class DateRangePickerState(rx.State):
    """State for the date range picker component."""
    current_month: datetime.date = datetime.date.today().replace(day=1)
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None

    # --- Computed Vars ---

    @rx.var
    def today_obj(self) -> datetime.date:
        return datetime.date.today()

    @rx.var
    def today_tuple(self) -> Tuple[int, int, int]:
        today = self.today_obj
        return (today.year, today.month, today.day)

    @rx.var
    def start_date_tuple(self) -> Optional[Tuple[int, int, int]]:
        if self.start_date:
            return (self.start_date.year, self.start_date.month, self.start_date.day)
        return None

    @rx.var
    def end_date_tuple(self) -> Optional[Tuple[int, int, int]]:
        if self.end_date:
            return (self.end_date.year, self.end_date.month, self.end_date.day)
        return None

    @rx.var
    def is_range_complete(self) -> bool:
        return self.start_date is not None and self.end_date is not None

    @rx.var
    def current_month_str(self) -> str:
        return self.current_month.strftime("%B %Y")

    @rx.var
    def selected_range_str(self) -> str:
        if self.start_date and self.end_date:
            s = min(self.start_date, self.end_date)
            e = max(self.start_date, self.end_date)
            # Format matches the image: Apr 01, 2025 - Apr 19, 2025
            return f"{s.strftime('%b %d, %Y')} - {e.strftime('%b %d, %Y')}"
        elif self.start_date:
             # Consistent format for single selection
            return f"{self.start_date.strftime('%b %d, %Y')} - ..."
        else:
            return ""

    @rx.var
    def calendar_grid_days(self) -> List[Tuple[int, Tuple[int, int, int], str]]:
        """
        Generate the days for the calendar grid with a status string.
        Returns a list of tuples: (day_number, date_tuple, status_string)
        Status strings: "start", "end", "single_day_range", "in_range", "today", "current_month", "other_month"
        """
        days_data = []
        year = self.current_month.year
        month = self.current_month.month
        first_day_weekday = calendar.weekday(year, month, 1)
        start_cal_date = self.current_month - datetime.timedelta(days=first_day_weekday)

        ordered_start = None
        ordered_end = None
        if self.start_date and self.end_date:
            ordered_start = min(self.start_date, self.end_date)
            ordered_end = max(self.start_date, self.end_date)
        elif self.start_date:
            ordered_start = self.start_date
            # If only start is selected, still check for range status based on it
            ordered_end = self.start_date


        today_date = self.today_obj
        current_cal_date = start_cal_date

        for _ in range(42):
            date_obj = current_cal_date
            date_tuple = (date_obj.year, date_obj.month, date_obj.day)
            day_num = date_obj.day
            is_current = date_obj.month == month
            status = ""

            if ordered_start and date_obj == ordered_start:
                if ordered_end and date_obj == ordered_end:
                    status = "single_day_range"
                else:
                    status = "start"
            elif ordered_end and date_obj == ordered_end:
                 status = "end"
            elif ordered_start and ordered_end and ordered_start < date_obj < ordered_end:
                 status = "in_range"
            elif is_current:
                # Check for today status only if not part of a selected range
                if date_obj == today_date:
                    status = "today"
                else:
                    status = "current_month"
            else:
                status = "other_month"

            days_data.append((day_num, date_tuple, status))
            current_cal_date += datetime.timedelta(days=1)
        return days_data

    # --- Event Handlers (unchanged) ---
    @rx.event
    def previous_month(self):
        current_year = self.current_month.year
        current_m = self.current_month.month
        if current_m == 1:
            self.current_month = self.current_month.replace(year=current_year - 1, month=12, day=1)
        else:
            self.current_month = self.current_month.replace(month=current_m - 1, day=1)

    @rx.event
    def next_month(self):
        current_year = self.current_month.year
        current_m = self.current_month.month
        if current_m == 12:
            self.current_month = self.current_month.replace(year=current_year + 1, month=1, day=1)
        else:
            self.current_month = self.current_month.replace(month=current_m + 1, day=1)

    @rx.event
    def select_date(self, date_tuple: Tuple[int, int, int]):
        try:
            year, month, day = date_tuple
            clicked_date = datetime.date(year, month, day)

            if self.is_range_complete:
                self.start_date = clicked_date
                self.end_date = None
            elif self.start_date is None:
                self.start_date = clicked_date
            else:
                self.end_date = clicked_date

        except (TypeError, ValueError) as e:
             print(f"Error converting date_tuple in select_date: {date_tuple}, Error: {e}")

    @rx.event
    def go_to_today(self):
        today_date = self.today_obj
        self.current_month = today_date.replace(day=1)
        self.start_date = None
        self.end_date = None

    @rx.event
    def cancel(self):
        self.start_date = None
        self.end_date = None

    @rx.event
    def apply(self):
        if self.is_range_complete:
            s = min(self.start_date, self.end_date)
            e = max(self.start_date, self.end_date)
            print(f"Date range applied: {s} to {e}")
        else:
            print("Apply clicked but range is not complete.")


# --- Components ---

def day_cell(day_data: rx.Var[Tuple[int, Tuple[int, int, int], str]]) -> rx.Component:
    """
    Renders a single day cell using rx.match based on status.
    day_data tuple: (day_num, date_tuple, status_string)
    """
    day_num = day_data[0]
    date_tuple = day_data[1]
    status = day_data[2]

    base_button_classes = "w-8 h-8 flex items-center justify-center text-sm font-medium transition-colors duration-150 ease-in-out"

    # Refined styles based on the image
    button_style_class = rx.match(
        status,
        ("start", f"{base_button_classes} bg-purple-600 text-white rounded-l-full"),
        ("end", f"{base_button_classes} bg-purple-600 text-white rounded-r-full"),
        ("single_day_range", f"{base_button_classes} bg-purple-600 text-white rounded-full"),
        # In-range dates: Default text color, transparent background on the button itself
        ("in_range", f"{base_button_classes} bg-transparent text-gray-800 rounded-none"),
         # Today: Slightly bolder text or different color? Let's try default text but bold. Add hover.
        ("today", f"{base_button_classes} bg-transparent text-gray-800 rounded-full hover:bg-gray-100 font-semibold"),
        # Current month: Default text, add hover
        ("current_month", f"{base_button_classes} bg-transparent text-gray-800 rounded-full hover:bg-gray-100"),
        # Other month: Dimmed text
        f"{base_button_classes} bg-transparent text-gray-400 rounded-full" # Default case
    )

    # Outer div controls the background highlight for the range
    outer_div_class = rx.match(
        status,
        # Apply light purple background only for days truly between start and end
        ("in_range", "bg-purple-100 w-full h-8 flex items-center justify-center"),
        # Default: No extra background, just layout
        "flex items-center justify-center h-8"
    )

    return rx.el.div(
         rx.el.button(
             day_num,
             on_click=lambda: DateRangePickerState.select_date(date_tuple),
             class_name=button_style_class,
             disabled=(status == "other_month"), # Disable clicking days in other months
         ),
         class_name=outer_div_class
    )


def calendar_header() -> rx.Component:
    # (No changes needed)
    return rx.el.div(
        rx.el.button(
            rx.el.svg(
                rx.el.path(
                    stroke_linecap="round",
                    stroke_linejoin="round",
                    stroke_width="2",
                    d="M15 19l-7-7 7-7"
                ),
                class_name="w-5 h-5 text-gray-600 hover:text-gray-800",
                fill="none",
                view_box="0 0 24 24",
                stroke="currentColor",
            ),
            on_click=DateRangePickerState.previous_month,
            class_name="p-1 rounded hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-1 focus:ring-purple-500 transition-colors duration-150 ease-in-out"
        ),
        rx.el.p(
            DateRangePickerState.current_month_str,
            class_name="text-sm font-semibold text-gray-800" # Use slightly darker text
        ),
        rx.el.button(
             rx.el.svg(
                rx.el.path(
                    stroke_linecap="round",
                    stroke_linejoin="round",
                    stroke_width="2",
                    d="M9 5l7 7-7 7"
                ),
                class_name="w-5 h-5 text-gray-600 hover:text-gray-800",
                fill="none",
                view_box="0 0 24 24",
                stroke="currentColor",
            ),
            on_click=DateRangePickerState.next_month,
            class_name="p-1 rounded hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-1 focus:ring-purple-500 transition-colors duration-150 ease-in-out"
        ),
        class_name="flex justify-between items-center mb-3 px-2"
    )

def week_days_header() -> rx.Component:
     # (No changes needed)
    return rx.el.div(
        rx.foreach(
            WEEKDAYS,
            lambda day: rx.el.div(
                day,
                # Slightly darker weekday header text
                class_name="w-8 text-center text-xs font-medium text-gray-600"
            )
        ),
        class_name="grid grid-cols-7 gap-y-1 mb-2 px-1 justify-items-center"
    )

def calendar_grid() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            DateRangePickerState.calendar_grid_days,
            day_cell
        ),
        # Ensure no vertical gap for continuous range background
        class_name="grid grid-cols-7 px-1 justify-items-center"
    )

def date_range_picker() -> rx.Component:
    return rx.el.div(
        calendar_header(),
        rx.el.div( # Input-like display + Today button
             rx.el.div(
                 rx.cond(
                     DateRangePickerState.start_date,
                     # Display formatted range string
                     rx.el.p(DateRangePickerState.selected_range_str, class_name="text-sm text-gray-800 truncate"), # truncate if too long
                     rx.el.p("Select start date", class_name="text-sm text-gray-400")
                 ),
                 # Slightly different border/padding to match image?
                 class_name="flex-grow border border-gray-300 rounded-md px-3 py-1.5 mr-2 h-9 flex items-center bg-white"
             ),
             rx.el.button(
                "Today",
                on_click=DateRangePickerState.go_to_today,
                # Match button style from image
                class_name="px-4 py-1.5 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-1 focus:ring-purple-500 h-9 transition-colors duration-150 ease-in-out"
            ),
            class_name="flex items-center mb-4 px-1"
        ),
        week_days_header(),
        calendar_grid(),
        # Use slightly thinner divider maybe? my-3 instead of my-4
        rx.el.div(class_name="my-3 border-t border-gray-200"),
        rx.el.div( # Footer buttons
            rx.el.button(
                "Cancel",
                on_click=DateRangePickerState.cancel,
                 # Match Cancel button style
                 class_name="px-4 py-1.5 border border-gray-300 rounded-md text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-1 focus:ring-purple-500 transition-colors duration-150 ease-in-out"
            ),
            rx.el.button(
                "Apply",
                on_click=DateRangePickerState.apply,
                class_name=rx.cond(
                    ~DateRangePickerState.is_range_complete,
                    # Match Apply button style (disabled) - brighter purple? Maybe 500->300 is too much dimming. Try 400?
                    "px-4 py-1.5 bg-purple-400 text-white rounded-md text-sm font-medium cursor-not-allowed",
                     # Match Apply button style (enabled) - use a brighter purple like 500 or 600
                    "px-4 py-1.5 bg-purple-600 text-white rounded-md text-sm font-medium hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-1 focus:ring-purple-500 transition-colors duration-150 ease-in-out"
                ),
                 disabled=~DateRangePickerState.is_range_complete
            ),
            class_name="flex justify-end space-x-2 px-1"
        ),
        # Main container styling, maybe slightly less padding? p-3 instead of p-4
        class_name="bg-white p-3 rounded-lg shadow-md max-w-xs mx-auto border border-gray-200"
    )

# --- App Definition ---

# def index() -> rx.Component:
#     return rx.el.div(
#         date_range_picker(),
#         class_name="p-10 bg-gray-100 min-h-screen flex items-center justify-center"
#     )

# app = rx.App(theme=rx.theme(appearance="light"))
# app.add_page(index, route="/")