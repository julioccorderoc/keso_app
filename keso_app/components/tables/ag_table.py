import reflex as rx
from ag_column_gen import generate_column_defs
import reflex_ag_grid as ag

# experimentar con filtros flotandes

# ag-grid table configuration

table_config = {
    "theme": "material",
    "suppress_movable_columns": True,
    "row_selection": "single",
    "pagination": True,
    "pagination_page_size": 10,
    "pagination_page_size_selector": [10, 20, 50],
    "width": "90%",
    "height": "80vh",
}

def ag_table(
    table_id: str,
    row_data: list,
    column_defs: list,
    ):
    return ag(
        id = table_id,
        row_data = row_data,
        column_defs = column_defs,
        **table_config,
    )