
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

from components.filters import *
from components.summary_stats import *
from components.map import *

import pandas as pd
from controls import PERIODS

df = pd.read_csv('data/scores-cities.csv')

def build_simulator():
    return [
        html.H6("Simulation tool"),
        html.Div(
            [
                filters_simulator(),
                html.Div(
                    [
                        dcc.Graph(
                            id='prediction-graph',
                            # figure={
                            #     'data': {},
                            #     'layout': go.Layout(
                            #         title='Expected ICFES Results',
                            #         xaxis=go.layout.XAxis(
                            #             tickangle=45,
                            #             title_text="Periodo",
                            #         )
                            #     )
                            # },
                        )
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            id="filters-and-map",
            className="row flex-display",
        )
    ]


y_predicted_model1 = [261, 266, 267, 269, 267, 287, 270, 262, 263,
                      264, 265, 268, 268, 273, 274, 273, 274, 277, 282, 283, 273, 271, 270]
y_current = [261, 266, 267, 269, 267, 287, 270, 262, 263, 264,
             265, 268, 268, 273, 274, 273, 274, 277, 282, 283, 273, 271]


def getScores(municipioCode):
    lista = df[df.COLE_COD_MPIO_COLEGIO==municipioCode].PUNT_GLOBAL.unique()
    return list(lista)

def getPeriods(municipioCode):
    lista = df[df.COLE_COD_MPIO_COLEGIO==municipioCode].PERIODO.unique()
    return [each.replace('-', '_') for each in lista]


def getSimpleVariables():
    response = [
        html.Div(
            [
                html.P("ESTU_TRABAJA:", className="control_label"),
                dcc.Input(id='range-ESTU_TRABAJA', type='number',
                          min=0, max=100, step=0.1),
            ],
            className="row flex-display",
        ),
        html.Br(),
        html.Div(
            [
                html.P("FAMI_TIENEINTERNET:", className="control_label"),
                dcc.Input(id='range-FAMI_TIENEINTERNET', type='number',
                          min=0, max=100, step=0.1),
            ],
            className="row flex-display",
        ),
        html.Br(),
        html.Div(
            [
                html.P("COBERTURA_NETA:", className="control_label"),
                dcc.Input(id='range-COBERTURA_NETA', type='number',
                          min=0, max=100, step=0.1),
            ],
            className="row flex-display",
        ),
        html.Br()
    ]
    return response


def getAdvancedVariables():
    response = [
        html.Div(
            [
                html.P("ESTU_TRABAJA:", className="control_label"),
                dcc.Input(id='range-ESTU_TRABAJA', type='number',
                          min=0, max=100, step=0.1),
            ],
            className="row flex-display",
        ),
        html.Br(),
        html.Div(
            [
                html.P("FAMI_TIENEINTERNET:", className="control_label"),
                dcc.Input(id='range-FAMI_TIENEINTERNET', type='number',
                          min=0, max=100, step=0.1),
            ],
            className="row flex-display",
        ),
        html.Br(),
        html.Div(
            [
                html.P("COBERTURA_NETA:", className="control_label"),
                dcc.Input(id='range-COBERTURA_NETA', type='number',
                          min=0, max=100, step=0.1),
            ],
            className="row flex-display",
        ),
        html.Br(),
        html.Div([html.P("FAMI_ESTRATO_VIVIENDA:", className="control_label"), dcc.Input(
            id="range-FAMI_ESTRATO_VIVIENDA", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_PERSONAS_HOGAR:", className="control_label"), dcc.Input(
            id="range-FAMI_PERSONAS_HOGAR", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_TIENEAUTOMOVIL:", className="control_label"), dcc.Input(
            id="range-FAMI_TIENEAUTOMOVIL", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_TIENECOMPUTADOR:", className="control_label"), dcc.Input(
            id="range-FAMI_TIENECOMPUTADOR", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_TIENELAVADORA:", className="control_label"), dcc.Input(
            id="range-FAMI_TIENELAVADORA", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_TIENE_HORNO_MICROONDAS:", className="control_label"), dcc.Input(
            id="range-FAMI_TIENE_HORNO_MICROONDAS", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_TIENETELEVISOR:", className="control_label"), dcc.Input(
            id="range-FAMI_TIENETELEVISOR", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_MADRE_Postgrado:", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_MADRE_Postgrado", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_MADRE_Preescolar:", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_MADRE_Preescolar", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_MADRE_Primaria:", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_MADRE_Primaria", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_MADRE_Secundaria (Bachillerato):", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_MADRE_Secundaria (Bachillerato)", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_MADRE_Titulo universitario:", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_MADRE_Titulo universitario", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_MADRE_Técnico o tecnológico:", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_MADRE_Técnico o tecnológico", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_PADRE_Postgrado:", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_PADRE_Postgrado", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_PADRE_Preescolar:", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_PADRE_Preescolar", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_PADRE_Primaria:", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_PADRE_Primaria", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_PADRE_Secundaria (Bachillerato):", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_PADRE_Secundaria (Bachillerato)", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_PADRE_Titulo universitario:", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_PADRE_Titulo universitario", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_EDUCA_PADRE_Técnico o tecnológico:", className="control_label"), dcc.Input(
            id="range-FAMI_EDUCA_PADRE_Técnico o tecnológico", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_OCUPA_MADRE_Hogar:", className="control_label"), dcc.Input(
            id="range-FAMI_OCUPA_MADRE_Hogar", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("FAMI_OCUPA_PADRE_Hogar:", className="control_label"), dcc.Input(
            id="range-FAMI_OCUPA_PADRE_Hogar", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("ESTU_JORNADA_MAÑANA:", className="control_label"), dcc.Input(
            id="range-ESTU_JORNADA_MAÑANA", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("ESTU_JORNADA_NOCHE:", className="control_label"), dcc.Input(
            id="range-ESTU_JORNADA_NOCHE", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("ESTU_JORNADA_SABATINA-DOMINICAL:", className="control_label"), dcc.Input(
            id="range-ESTU_JORNADA_SABATINA-DOMINICAL", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("ESTU_JORNADA_TARDE:", className="control_label"), dcc.Input(
            id="range-ESTU_JORNADA_TARDE", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("ESTU_JORNADA_UNICA:", className="control_label"), dcc.Input(
            id="range-ESTU_JORNADA_UNICA", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("DESERCION:", className="control_label"), dcc.Input(
            id="range-DESERCION", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("APROBACION:", className="control_label"), dcc.Input(
            id="range-APROBACION", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("COLE_CATEGORIA_N:", className="control_label"), dcc.Input(
            id="range-COLE_CATEGORIA_N", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("COLE_BILINGUE:", className="control_label"), dcc.Input(
            id="range-COLE_BILINGUE", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("COLE_PAGA_PENSION:", className="control_label"), dcc.Input(
            id="range-COLE_PAGA_PENSION", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("COLE_NSE:", className="control_label"), dcc.Input(
            id="range-COLE_NSE", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br(),
        html.Div([html.P("COLE_NATURALEZA_OFICIAL:", className="control_label"), dcc.Input(
            id="range-COLE_NATURALEZA_OFICIAL", type="number", min=0, max=100, step=0.1)], className="row flex-display"), html.Br()]
    return response
