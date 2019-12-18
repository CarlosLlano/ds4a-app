
import dash_core_components as dcc
import dash_html_components as html

from components.filters import *
from components.summary_stats import *
from components.map import *
from components.dashboardDetailed import *


def build_dashboard():
    return [
        html.H6("General analysis"),
        html.Br(),
        html.P("Here you can see a behaviour over time of the icfes results and different socioeconomic factors in all Colombia"),
        html.Div(
            [
                filters(),
                html.Div(
                    [
                        summary_info(),
                        map(),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            id="filters-and-map",
            className="row flex-display",
        ),
        build_dashboard_detailed()
    ]
