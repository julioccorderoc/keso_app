import reflex as rx
from ..states import routes
from .. import styles
from ..template.base import create_page




import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/GanttChart-updated.csv"
)

column_defs = [
    ag_grid.column_def(field="Task", filter=True),
    ag_grid.column_def(
        field="Start", filter=ag_grid.filters.date
    ),
    ag_grid.column_def(
        field="Duration", filter=ag_grid.filters.number
    ),
    ag_grid.column_def(
        field="Resource", filter=ag_grid.filters.text
    ),
]

@create_page(route=routes.CONTACT_ROUTE, title="Contacto")
def contact():
    return ag_grid(
        id="ag_grid_basic_column_filtering",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="100%",
        height="60vh",
    )