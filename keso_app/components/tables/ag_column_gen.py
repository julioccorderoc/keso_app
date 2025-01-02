from header_mapping import HEADER, TYPE, CONFIG, FILTER, SORTABLE, HIDE, header_mapping
import reflex_ag_grid as ag

# Filter mapping

FILTERS_MAP = {
    "date": ag.filters.date,
    "number": ag.filters.number,
    "text": ag.filters.text
}

# Helper functions

def is_boolean(value):
    return isinstance(value, bool)

def get_default_column_def(field):
    """Creates a default column definition."""
    return ag.column_def(field=field, header_name=field, filter=True, sortable=True)

def get_config_value(config, key, default=None, type_check=None):
    """Gets a config value with a default and optional type check."""
    value = config.get(key, default)
    if type_check and not isinstance(value, type_check):
        return default
    return value

# Main function

def generate_column_defs(data):
    if not data:
        return []

    first_item = data[0]
    column_defs = []
    for field in first_item.keys():
        field_config = header_mapping.get(field)

        if not field_config:  # Early exit if no field mapping
            print(f"Warning: No mapping found for field '{field}'. Using default configuration.")
            column_defs.append(get_default_column_def(field))
            continue

        config = field_config.get(CONFIG)
        if not config:  # Early exit if no config found
            print(f"Warning: No 'config' found for field '{field}'. Using default configuration.")
            column_defs.append(get_default_column_def(field))
            continue
        
        header_name = field_config.get(HEADER) or field
        type_value = field_config.get(TYPE)

        filter_value = get_config_value(config, FILTER, True, bool)
        if isinstance(filter_value, str) and filter_value in FILTERS_MAP:
            filter_param = FILTERS_MAP[filter_value]
        else:
            filter_param = filter_value

        sortable_value = get_config_value(config, SORTABLE, True, bool)
        hide_value = get_config_value(config, HIDE, False, bool)

        column_def = ag.column_def(
            field=field,
            header_name=header_name,
            type=type_value,
            filter=filter_param,
            sortable=sortable_value,
            hide=hide_value,
        )
        column_defs.append(column_def)

    return column_defs