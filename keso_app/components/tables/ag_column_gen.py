from reflex_ag_grid import ag_grid
from .header_mapping import HEADER, TYPE, CONFIG, FILTER, SORTABLE, HIDE, header_mapping
from typing import Dict, Any

# Filter mapping

FILTERS_MAP = {
    "date": ag_grid.filters.date,
    "number": ag_grid.filters.number,
    "text": ag_grid.filters.text
}

# Helper functions

def get_default_column_def(column_name):
    """Creates a default column definition."""
    return ag_grid.column_def(
        field=column_name, 
        header_name=column_name, 
        filter=False, 
        sortable=False,
        hide=False,
        flex=1
        )

# Main function

def generate_column_defs(sample_row):
    if not sample_row:
        return []

    column_defs = []
    
    for column_name in sample_row.keys():
        header_to_map = header_mapping.get(column_name)

        if not header_to_map:
            print(f"Warning: No mapping found for column_name '{column_name}'. Using default configuration.")
            column_defs.append(get_default_column_def(column_name))
            continue

        configuration_values = header_to_map.get(CONFIG)
        if not configuration_values:
            print(f"Warning: No 'configuration_values' found for column_name '{column_name}'. Using default configuration.")
            column_defs.append(get_default_column_def(column_name))
            continue
        
        # main values
        header_name = header_to_map.get(HEADER) or column_name
        type_value = header_to_map.get(TYPE)

        # configuration values (this lacks robust error handling and type validation)
        filter_value = configuration_values.get(FILTER)
        sortable_value = configuration_values.get(SORTABLE)
        hide_value = configuration_values.get(HIDE)

        column_def = ag_grid.column_def(
            field=column_name,
            header_name=header_name,
            type=type_value,
            filter=filter_value,
            sortable=sortable_value,
            hide=hide_value,
        )
        column_defs.append(column_def)

    return column_defs