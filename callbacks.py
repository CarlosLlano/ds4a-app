from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
from components.tabs import *
from components.map import *
from components.detailedgraphs import *
from components.simulator import *
from components.model import *
from controls import VARIABLES, CATEGORICAL_VARIABLES

dict_slider = {}
for i,each in enumerate(PERIODS):
    dict_slider[i] = each

def register_callbacks(app):

    # callback update_content
    @app.callback(
        Output("app-content", "children"),
        [
            Input("tabs", "value")
        ]
    )
    def update_content(tab_name):
        return build_content_for_tab(tab_name)

    # callback slider_value
    @app.callback(
        Output('periodos', 'children'),
        [
            Input("year_slider", "value")
        ]
    )
    def slider_value(value):
        start = dict_slider[value[0]].replace('_', '-')
        end = dict_slider[value[1]].replace('_', '-')
        selected = '{} - {}'.format(start, end)
        return [
            html.P(
                selected,
                className="control_label",
                id='periodo-selected',
                style={'font-weight': 'bold'}
            )
        ]
    
    # callback variables_type
    @app.callback(
        [
            Output('variables-dropdown', 'options')
        ],
        [
            Input("variables-type", "value")
        ]
    )
    def variables_type(value):
        variables = sorted((VARIABLES[value]))
        response = []
        options = [
            {"label": str(var), "value": str(var)} for var in variables
        ]
        response.append(options)
        return response


    # callback variables_dropdown
    @app.callback(
        [
            Output('div-categorical-variables', 'children')
        ],
        [
            Input("variables-dropdown", "value")
        ]
    )
    def variables_dropdown(value):
        response = []
        if value in CATEGORICAL_VARIABLES.keys():
            variables = sorted((CATEGORICAL_VARIABLES[value]))
            options = [
                {"label": str(var), "value": str(var)} for var in variables
            ]
            response.append([
                html.Div(
                    [
                        html.P("Options:", className="control_label"),
                        dcc.Dropdown(
                            id="categorical-variables-dropdown",
                            multi=False,
                            options=options,
                            value=variables[0],
                            className="dcc_control",
                        )
                    ]
                )
            ])
            return response
        else:
            response.append([
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
                        style={'display':'none'}
                )
            ])
            return response

    # callback update_map
    @app.callback(
        [
            Output('map', 'figure'),
            Output("average-text", "children"),
            Output("maximum-text", "children"),
            Output("minimum-text", "children"),
            Output("standard-deviation", "children")
        ],
        [
            Input("geographic-dropdown", "value"),
            Input("variables-dropdown", "value"),
            Input("categorical-variables-dropdown", "value"),
            Input("year_slider", "value")
        ]
    )
    def update_map(geographicValue, variable, variableOption, sliderValue):
        startPeriod = dict_slider[sliderValue[0]].replace('_', '-')
        endPeriod = dict_slider[sliderValue[1]].replace('_', '-')
        if variable in CATEGORICAL_VARIABLES.keys():
            var = str(variable) + '_' + str(variableOption)
            figure, average, maximum, minimum, std = get_map_data(geographicValue, var, startPeriod, endPeriod)
            return figure, average, maximum, minimum, std
        else:
            figure, average, maximum, minimum, std = get_map_data(geographicValue, variable, startPeriod, endPeriod)
            return figure, average, maximum, minimum, std


    @app.callback(
        [
            Output('city-dashboard-detailed', 'options')
        ],
        [
            Input("department-dashboard-detailed", "value")
        ]
    )
    def update_city_options(value):
        if value in citiesPerDepartment.keys():
            variables = sorted(citiesPerDepartment[value])
            options = [
                {"label": str(var), "value": str(var)} for var in variables
            ]
            return [options]   
        return [[]]


    @app.callback(
        [
            Output('detailed-scatter', 'figure')
        ],
        [
            Input("department-dashboard-detailed", "value"),
            Input("city-dashboard-detailed", "value"),
            Input("variables-dashboard-detailed", "value"),
            Input("puntajes-dashboard-detailed", "value")
        ]
    )
    def generateScatter(dptoValue, cityValue, variableValue, scoreValue):
        figure = go.Figure()
        if None not in (dptoValue, cityValue, variableValue, scoreValue):
            #por ciudad
            figure = getDetailedScatterByCity(cityValue, variableValue, scoreValue)
        elif None not in (dptoValue, variableValue, scoreValue):
            #por departamento
            figure = getDetailedScatterByDpto(dptoValue, variableValue, scoreValue)
        elif None not in (variableValue, scoreValue):
            #por pais
            figure = getDetailedScatterAllCountry(variableValue, scoreValue)

        return [figure]


    @app.callback(
        [
            Output('detailed-heatmap', 'figure')
        ],
        [
            Input("department-dashboard-detailed", "value"),
            Input("city-dashboard-detailed", "value"),
            Input("puntajes-dashboard-detailed", "value")
        ]
    )
    def generateHeatmap(dptoValue, cityValue, scoreValue):
        figure = go.Figure()
        if None not in (dptoValue, cityValue, scoreValue):
            figure = getHeatmapByCity(scoreValue, cityValue)
        elif None not in (dptoValue, scoreValue):
            figure = getHeatmapByDpto(scoreValue, dptoValue)
        elif scoreValue is not None:
            figure = getHeatmapAllCountry(scoreValue)
        return [figure]

    
    # callback variables_type
    @app.callback(
        [
            Output('variables-simulator', 'children')
        ],
        [
            Input("simulation-type", "value")
        ]
    )
    def simulation_type(value):
        response = []
        if value == 'Simple':
            variables = getSimpleVariables()
            response.append(variables)
            return [variables]
        else:
            variables = getAdvancedVariables()
            response.append(variables)
            return [variables]


    # @app.callback(
    #     Output('prediction-graph', 'figure'),
    #     [
    #         Input('city-dropdown-simulator', 'value'),
    #         Input('range-ESTU_TRABAJA', 'value'),
    #         Input('range-FAMI_TIENEINTERNET', 'value'),
    #         Input('range-COBERTURA_NETA', 'value'),
    #     ]
    # )
    # def update_output(city, estuTrabaja, tieneInternet, cobertura):
    #     figure = go.Figure()
    #     if None in (city, estuTrabaja, tieneInternet, cobertura):
    #         VariablesACambiar={
    #             'ESTU_TRABAJA':estuTrabaja,
    #             'FAMI_TIENECOMPUTADOR':tieneInternet,
    #             'COBERTURA_NETA':cobertura
    #         }
    #         predicted = PredecirMunicipio(city, VariablesACambiar=VariablesACambiar)
            
    #         codigo = CodigoMunicipio[value]
    #         periodos = getPeriods(codigo)
    #         scores = getScores(codigo)
    #         figure.add_trace(
    #             go.Scatter(
    #             x=periodos,
    #             y=scores,
    #             name = 'current',
    #             mode = 'lines+markers',
    #         ))
    #         periodos.append('2019_2')
    #         scores.append(predicted)
    #         figure.add_trace(
    #             go.Scatter(
    #             x=periodos,
    #             y=scores,
    #             name = 'current',
    #             mode = 'lines+markers',
    #         ))
        
    #     return figure

    # @app.callback(
    #     Output('prediction-graph', 'figure'),
    #     [
    #         Input('city-dropdown-simulator', 'value'),
    #         Input('range-ESTU_TRABAJA', 'value'),
    #         Input('range-FAMI_TIENEINTERNET', 'value'),
    #         Input('range-COBERTURA_NETA', 'value'),
    #     ]
    # )
    # def update_output(city, estuTrabaja, tieneInternet, cobertura):
    #     figure = go.Figure()
    #     if city is not None:
    #         codigo = CodigoMunicipio[city]
    #         periodos = getPeriods(codigo)
    #         scores = getScores(codigo)
    #         # data = scatter_plot_simulator(periodos, scores)
    #         figure.add_trace(
    #             go.Scatter(
    #             x=periodos,
    #             y=scores,
    #             name = 'current',
    #             mode = 'lines+markers',
    #         ))

    #     if None in (city, estuTrabaja, tieneInternet, cobertura):
    #         estuTrabaja = float(estuTrabaja)
    #         tieneInternet = float(tieneInternet)
    #         cobertura = float(cobertura)
    #         VariablesACambiar={
    #             'ESTU_TRABAJA': estuTrabaja,
    #             'FAMI_TIENECOMPUTADOR': tieneInternet,
    #             'COBERTURA_NETA': cobertura
    #         }
    #         predicted = PredecirMunicipio(city, VariablesACambiar=VariablesACambiar)
    #         codigo = CodigoMunicipio[city]
    #         periodos = getPeriods(codigo)
    #         scores = getScores(codigo)
    #         periodos.append('2019_2')
    #         scores.append(predicted)
    #         figure.add_trace(
    #             go.Scatter(
    #             x=periodos,
    #             y=scores,
    #             name = 'model',
    #             mode = 'lines+markers',
    #         ))

    #     return figure

    @app.callback(
        Output('prediction-graph', 'figure'),
        [
            Input('city-dropdown-simulator', 'value'),
            Input('range-ESTU_TRABAJA', 'value'),
            Input('range-FAMI_TIENEINTERNET', 'value'),
            Input('range-COBERTURA_NETA', 'value'),
        ]
    )
    def update_output(value, estuTrabaja, tieneInternet, cobertura):
        figure = go.Figure()
        if value is not None:
            codigo = CodigoMunicipio[value]
            periodos = getPeriods(codigo)
            scores = getScores(codigo)
            # data = scatter_plot_simulator(periodos, scores)
            figure.add_trace(
                go.Scatter(
                x=periodos,
                y=scores,
                name = 'current',
                mode = 'lines+markers',
            ))

        if None not in (value, estuTrabaja, tieneInternet, cobertura):
            periodos = getPeriods(codigo)
            scores = getScores(codigo)
            predicted = np.random.randint(250, 300)
            periodos.append('2019-1')
            print(periodos)
            scores.append(predicted)
            print(scores)
            figure.add_trace(
                go.Scatter(
                x=periodos,
                y=scores,
                name = 'model',
                mode = 'lines+markers',
            ))

        return figure