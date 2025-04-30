from keso_app.constants.shared import NO_FILTER_LABEL, NO_FILTER_VALUE, ColumnConfig, TableConstants


TABLE_NAME = "vw_cheese_production"

FILTER_COMMENTS_OPTIONS = {
    NO_FILTER_LABEL: NO_FILTER_VALUE,
    "Llanero": "llanero",
    "Guayanes": "guayanes",
    "Telita": "telita" 
}

COLUMN_CONFIG: dict[str, ColumnConfig] = {
    "batch_id": ColumnConfig(
        label="Batch ID",
        tag="ID",
        default_sort=False,
        visible=False,
        sortable=False,
        filterable=False,
        searchable=False,
        filter_options=None
    ),
    "batch_date": ColumnConfig(
        label="Batch Date",
        tag="Date",
        default_sort=True,
        visible=True,
        sortable=True,
        filterable=False,
        searchable=False,
        filter_options=None
    ),
    "kilos_of_cheese": ColumnConfig(
        label="Cheese (kg)",
        tag="Cheese",
        default_sort=False,
        visible=True,
        sortable=True,
        filterable=False,
        searchable=False,
        filter_options=None
    ),
    "liters_per_kilo": ColumnConfig(
        label="Milk/Cheese Ratio (L/Kg)",
        tag="Milk/Cheese",
        default_sort=False,
        visible=True,
        sortable=True,
        filterable=False,
        searchable=False,
        filter_options=None
    ),
    "salt_per_liter": ColumnConfig(
        label="Salt/Milk Ratio (Kg/L)",
        tag="Salt/Milk",
        default_sort=False,
        visible=True,
        sortable=True,
        filterable=False,
        searchable=False,
        filter_options=None
    ),
    "comments": ColumnConfig(
        label="Comments",
        tag="Comments",
        default_sort=False,
        visible=True,
        sortable=True,
        filterable=True,
        searchable=True,
        filter_options=FILTER_COMMENTS_OPTIONS,
    ),
}

CHEESE_CONSTANTS = TableConstants(
    table_name = TABLE_NAME, 
    column_config = COLUMN_CONFIG
)


if __name__ == "__main__":
    print(f"\nVisible columns: \n{CHEESE_CONSTANTS.visible_columns}\n\n")
    print(f"Sortable columns: \n{CHEESE_CONSTANTS.sortable_columns}\n\n")
    print(f"Searchable columns: \n{CHEESE_CONSTANTS.searchable_columns}\n\n")
    print(f"Filterable columns: \n{CHEESE_CONSTANTS.filters_for_ui}\n\n")
    print(f"Default sort column: \n{CHEESE_CONSTANTS.default_sort_column}\n\n")