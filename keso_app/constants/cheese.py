from enum import StrEnum
from typing import Any

from keso_app.constants.shared import NO_FILTER_LABEL, NO_FILTER_VALUE

DATA_SOURCE = "vw_cheese_production"

class COL_NAMES(StrEnum):
    BATCH_ID = "batch_id"
    BATCH_DATE = "batch_date"
    KILOS = "kilos_of_cheese"
    LITERS_RATIO = "liters_per_kilo"
    SALT_RATIO = "salt_per_liter"
    COMMENTS = "comments"

# Order: label - value
FILTER_COMMENTS_OPTIONS = {
    NO_FILTER_LABEL: NO_FILTER_VALUE,
    "Llanero": "llanero",
    "Guayanes": "guayanes",
    "Telita": "telita" 
}

COLUMN_MAPPING: dict[str, dict[str, str | bool | None]] = {
    "batch_id": {
        "label": "Batch ID",
        "tag": "ID",
        "default_sort": False,
        "visible": False,
        "sortable": False,
        "filterable": False,
        "searchable": False,
        "filter_options": None,
    },
    "batch_date": {
        "label": "Batch Date",
        "tag": "Date",
        "default_sort": True,
        "visible": True,
        "sortable": True,
        "filterable": False,
        "searchable": False,
        "filter_options": None,
    },
    "kilos_of_cheese": {
        "label": "Cheese (kg)",
        "tag": "Cheese",
        "default_sort": False,
        "visible": True,
        "sortable": True,
        "filterable": False,
        "searchable": False,
        "filter_options": None,
    },
    "liters_per_kilo": {
        "label": "Milk/Cheese Ratio (L/Kg)",
        "tag": "Milk/Cheese",
        "default_sort": False,
        "visible": True,
        "sortable": True,
        "filterable": False,
        "searchable": False,
        "filter_options": None,
    },
    "salt_per_liter": {
        "label": "Salt/Milk Ratio (Kg/L)",
        "tag": "Salt/Milk",
        "default_sort": False,
        "visible": True,
        "sortable": True,
        "filterable": False,
        "searchable": False,
        "filter_options": None,
    },
    "comments": {
        "label": "Comments",
        "tag": "Comments",
        "default_sort": False,
        "visible": True,
        "sortable": True,
        "filterable": True,
        "searchable": True,
        "filter_options": FILTER_COMMENTS_OPTIONS,
    },
}


VISIBLE_COLUMNS: list[str] = [
    col_name for col_name, config in COLUMN_MAPPING.items() if config.get("visible", False)
]

VISIBLE_COLUMN_CONFIGS: list[tuple[str, dict[str, Any]]] = [
    (col_name, config)
    for col_name, config in COLUMN_MAPPING.items()
    if config.get("visible", False)
]

# Set of column *string names* allowed for sorting
ALLOWED_SORT_COLUMNS: set[str] = {
    col_enum for col_enum, config in COLUMN_MAPPING.items() if config.get("sortable", False)
}

# list of column *string names* used for text search
SEARCHABLE_COLUMNS: set[str] = {
    col_enum for col_enum, config in COLUMN_MAPPING.items() if config.get("searchable", False)
}

# Dictionary defining filters for UI generation (similar to previous FILTER_CONFIG)
# Key: column string name, Value: {'label': 'Filter Label', 'options': {label:value}}
FILTERS_FOR_UI: dict[str, dict[str, str]] = {
    col_enum: {
        "options": config.get("filter_options")
    }
    for col_enum, config in COLUMN_MAPPING.items()
    if config.get("filterable", False) and config.get("filter_options") is not None
}

# Determine the default sort column string name
DEFAULT_SORT_COLUMN_STR: str = next(
    (col_enum for col_enum, config in COLUMN_MAPPING.items() if config.get("default_sort")),
    # Fallback to the first sortable column if none marked as default
    next((col_enum for col_enum, config in COLUMN_MAPPING.items() if config.get("sortable")), None)
)

if __name__ == "__main__":
    print(VISIBLE_COLUMNS)