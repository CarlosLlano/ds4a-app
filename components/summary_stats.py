import dash_core_components as dcc
import dash_html_components as html

def summary_info():
    return html.Div(
        [
            html.Div(
                [
                    html.H6(id="average-text"),
                    html.P("Average")
                ],
                id="media",
                className="mini_container",
            ),
            html.Div(
                [
                    html.H6(id="maximum-text"), 
                    html.P("Maximum")
                ],
                id="max",
                className="mini_container",
            ),
            html.Div(
                [
                    html.H6(id="minimum-text"), 
                    html.P("Minimum")
                ],
                id="min",
                className="mini_container",
            ),
            html.Div(
                [
                    html.H6(id="standard-deviation"), 
                    html.P("Standard Deviation")
                ],
                id="std",
                className="mini_container",
            ),
        ],
        id="info-container",
        className="row container-display",
    )