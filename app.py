# pandas
import pandas as pd
# dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.graph_objects as go

from components.tabs import *
from components.dashboard import *
from callbacks import register_callbacks

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server
app.config['suppress_callback_exceptions']=True

# Layout
app.layout = html.Div(
    [
        html.Div(id='hidden-div', style={'display':'none'}),
        dcc.Store(id="aggregate_data"),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),
        html.Div(
            [
                # left image
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("ds4A-logo.png"),
                            id="ds4A-logo-image",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        ),
                    ],
                    className="one-third column",
                ),
                # title
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "ICFES results analysis",
                                    style={"margin-bottom": "0px"},
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                    style={'display': 'block'}
                ),
                # tabs
                html.Div(
                    [
                        build_tabs()
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(children=build_dashboard(), id="app-content")
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)

register_callbacks(app)

# Main
if __name__ == "__main__":
    app.run_server(debug=True)
