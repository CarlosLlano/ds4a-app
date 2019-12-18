import dash_core_components as dcc
import dash_html_components as html

from components.filters import *


def build_dashboard_detailed():
    return html.Div(
        [
            html.H6("Detailed analysis"),
            html.Br(),
            html.P("Select variables to see the behaviour over time in specific departments or cities."),
            html.Div(
                [
                    filters_dashboard_detailed(),
                    html.Div(
                        [
                            dcc.Graph(id="detailed-scatter")
                        ],
                        className="pretty_container eight columns",
                    ),
                ],
                className="row flex-display",
            ),
            html.Br(),
            html.P('Best 15 and worst 15 perfomances.'),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(
                                id="detailed-heatmap",
                                style={
                                    "width": 600,
                                    "height": 800,
                                    "display": "block",
                                    "margin-left": "auto",
                                    "margin-right": "auto",
                                }
                            )
                        ],
                        className="pretty_container twelve columns",
                    )
                ],
                className="row flex-display",
            )
        ]
    )
