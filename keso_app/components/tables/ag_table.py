# import reflex as rx
from reflex_ag_grid import ag_grid
from .ag_column_gen import generate_column_defs
from typing import List, Dict, Any

# experimentar con filtros flotandes

# ag-grid table configuration

table_config = {
    "theme": "material",
    "suppress_movable_columns": True,
    "row_selection": "single",
    "pagination": True,
    "pagination_page_size": 10,
    "pagination_page_size_selector": [10, 20, 50],
    "width": "100%",
    "height": "100vh",
}

def ag_table(
    table_id: str,
    row_data: List[Dict[str, Any]]
    ):
    return ag_grid(
        id = table_id,
        row_data = row_data,
        column_defs = generate_column_defs(row_data[0]),
        **table_config,
    )