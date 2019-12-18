import dash_core_components as dcc
import dash_html_components as html
from controls import GEOGRAPHIC, DEPARTAMENTOS, PUNTAJES, VARIABLES_DETAILED_DASHBOARD
from components.slider import *
from components.model import *

geographic_options = [
    {"label": str(GEOGRAPHIC[geo]), "value": str(geo)} for geo in GEOGRAPHIC
]

departamentos_options = [
    {"label": str(dpto), "value": str(dpto)} for dpto in DEPARTAMENTOS
]

puntajes_options = [
    {"label": str(punt), "value": str(punt)} for punt in PUNTAJES
]

variables_options = [
    {"label": str(var), "value": str(var)} for var in VARIABLES_DETAILED_DASHBOARD
]

municipios_options = [
    {"label": str(var), "value": str(var)} for var in MUNICIPIOS
]


def filters():
    return html.Div(
        [
            html.H5(
                "Filters:",
                className="control_label",
            ),
            html.Div(
                [
                    html.P(
                        "Periods:",
                        className="control_label",
                    ),
                    html.Div(id='periodos')
                ]
            ),
            periods_slider(),

            html.Br(),

            html.P("Geographic level:", className="control_label"),

            dcc.Dropdown(
                id="geographic-dropdown",
                options=geographic_options,
                multi=False,
                value=GEOGRAPHIC['Department'],
                className="dcc_control",
                clearable=False
            ),
            html.P("Variable type:", className="control_label"),
            dcc.RadioItems(
                id="variables-type",
                options=[
                    {"label": "ICFES Scores", "value": "ICFES Scores"},
                    {"label": "Socioeconomic factors",
                        "value": "Socioeconomic factors"}
                ],
                value="ICFES Scores",
                className="dcc_control",
            ),
            html.P("Variables:", className="control_label"),
            dcc.Dropdown(
                id="variables-dropdown",
                multi=False,
                options=[],
                value='PUNT_GLOBAL',
                className="dcc_control",
                clearable=False
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Options:", className="control_label"),
                            dcc.Dropdown(
                                id="categorical-variables-dropdown",
                                multi=False,
                                options=[],
                                className="dcc_control",
                            )
                        ],
                        style={'display': 'none'}
                    )
                ],
                id='div-categorical-variables'
            )
        ],
        className="pretty_container four columns",
        id="cross-filter-options-dashboard",
    )


def filters_simulator():
    return html.Div(
        [
            html.P("City:", className="control_label"),
            dcc.Dropdown(
                id='city-dropdown-simulator',
                multi=False,
                options=municipios_options,
                className="dcc_control",
                placeholder="Select a city",
                clearable=False
            ),
            html.Br(),
            html.P('Type of simulation'),
            dcc.RadioItems(
                id='simulation-type',
                options=[
                    {"label": "Simple", "value": "Simple"},
                    {"label": "Advanced", "value": "Advanced"}
                ],
                value="Simple",
                className="dcc_control",
            ),
            html.Br(),
            html.P('Variables'),
            html.Div(id='variables-simulator', children=[]),
            html.Br(),
            html.Br(),
            #html.Button('Submit', id='button'),
            html.Button('Predict Next Period', id='prediction-button'),
        ],
        className="pretty_container four columns",
        id="cross-filter-options-simulator",
    )


def filters_dashboard_detailed():
    return html.Div(
        [
            html.P("Department (Optional):", className="control_label"),
            dcc.Dropdown(
                id='department-dashboard-detailed',
                multi=False,
                options=departamentos_options,
                className="dcc_control",
                placeholder="Select a department",
            ),
            html.P("City (Optional):", className="control_label"),
            dcc.Dropdown(
                id='city-dashboard-detailed',
                multi=False,
                className="dcc_control",
                placeholder="Select a city",
            ),
            html.P("Variable:", className="control_label"),
            dcc.Dropdown(
                id='variables-dashboard-detailed',
                options=variables_options,
                multi=False,
                className="dcc_control",
                placeholder="Select a variable",
            ),
            html.P("Scores:", className="control_label"),
            dcc.Dropdown(
                id='puntajes-dashboard-detailed',
                options=puntajes_options,
                multi=False,
                className="dcc_control",
                placeholder="Select a score",
            )
        ],
        className="pretty_container four columns",
    )
