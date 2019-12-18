# Create global chart template
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
from urllib.request import urlopen
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#Dataset
colegios = pd.read_csv('data/final-datos_colegio-cleaned.csv')
dpto_resumen = pd.read_csv('data/Resumen_Departamento.csv')
mcpio_resumen = pd.read_csv('data/Resumen_Municipio.csv')


#Mapbox token
mapbox_access_token = "pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w"

#geojson preparation
with open('data/municipios.geojson') as json_file:
        municipios = json.load(json_file)
for i, each in enumerate(municipios['features']):
    municipios['features'][i]['id']=municipios['features'][i]['properties']['MPIO_CCNCT']

with open('data/departamentos.geojson') as json_file:
        departamentos = json.load(json_file)
for i, each in enumerate(departamentos["features"]):
    departamentos["features"][i]['id']=departamentos["features"][i]['properties']['DPTO']

#annotations for maps
annotations = [
    dict(
        showarrow=False,
        align="right",
        text="<b>Age-adjusted death rate<br>per county per year</b>",
        font=dict(color="#000000"),
        bgcolor="#f9f9f9",
        x=0.95,
        y=0.95,
    )
]

def map():
    return html.Div(
        [
            dcc.Graph(id = "map", figure={})
        ],
        id="pretty_container seven columns",
        className="pretty_container",
    )

#Densitymapbox - colegio (lat, lon, puntaje-promedio (global, mat, etc))
#https://plot.ly/python/mapbox-density-heatmaps/
def map_colegios(df):
    tmp = df[['COLE_NOMBRE','LATITUD','LONGITUD']].copy()
    tmp['z'] = 1
    fig = go.Figure(go.Densitymapbox(lat=tmp['LATITUD'], lon=tmp['LONGITUD'], z=tmp['z'], radius=10))
    fig.update_layout(mapbox_style="stamen-terrain",
                    mapbox_center_lon=-74.2973328,
                    mapbox_center_lat=4.570868,
                    mapbox_zoom=4
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig
    
#departamentos - https://plot.ly/python/mapbox-county-choropleth/
def map_departamentos(df):
    fig = go.Figure(go.Choroplethmapbox(geojson=departamentos, 
                                        locations=df.COLE_COD_DEPTO, 
                                        z=df.COUNT,
                                        colorscale="Viridis",
                                        text=df.DEPARTAMENTO,
                                        marker_opacity=0.5, 
                                        marker_line_width=0))
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=4, 
        mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
        annotations=annotations)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

#municipios - https://plot.ly/python/mapbox-county-choropleth/
def map_municipios(df):
    fig = go.Figure(go.Choroplethmapbox(geojson=municipios, 
                                        locations=df.COLE_COD_MPIO_COLEGIO, 
                                        z=df.COUNT,
                                        colorscale="Viridis",
                                        text=df.MUNICIPIO,
                                        marker_opacity=0.5, 
                                        marker_line_width=0))
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=4, 
        mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
        annotations=annotations
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

# variables numerica
def get_map_data(geographicValue, variable, startPeriod, endPeriod):
    figure = {}
    average = 0
    maximum = 0
    minimum = 0
    std = 0

    if geographicValue == 'Department':
        if variable in dpto_resumen.columns:
            tmp = dpto_resumen[['COLE_COD_DEPTO', 'DEPARTAMENTO', 'PERIODO', 'CANTIDAD_ESTUDIANTES', variable]]
            tmp = tmp[(tmp.PERIODO >= startPeriod) & (tmp.PERIODO <= endPeriod)]
            tmp['FACTOR'] = tmp['CANTIDAD_ESTUDIANTES'] * tmp[variable]
            grouped = tmp.groupby(['COLE_COD_DEPTO','DEPARTAMENTO'], as_index=False)[['FACTOR', 'CANTIDAD_ESTUDIANTES']].mean()
            grouped[variable] = grouped['FACTOR'] / grouped['CANTIDAD_ESTUDIANTES']
            grouped.rename(columns={variable: 'COUNT'},inplace=True)
            grouped.COLE_COD_DEPTO = grouped.COLE_COD_DEPTO.apply(lambda x: str(x).zfill(2))
            
            average = round(grouped.COUNT.mean(), 2)
            maximum = round(grouped.COUNT.max(), 2)
            minimum = round(grouped.COUNT.min(), 2)
            std = round(grouped.COUNT.std(), 2)
            if maximum < 1:
                annotations[0]['text']='<b>{} of <br>{}</b>'.format('percentage', variable)
            else:
                annotations[0]['text']='<b>{} of <br>{}</b>'.format('average', variable)
            figure = map_departamentos(grouped)

    elif geographicValue == 'City':
         if variable in mcpio_resumen.columns:
            tmp = mcpio_resumen[['COLE_COD_MPIO_COLEGIO', 'MUNICIPIO', 'PERIODO', 'CANTIDAD_ESTUDIANTES', variable]]
            tmp = tmp[(tmp.PERIODO >= startPeriod) & (tmp.PERIODO <= endPeriod)]
            tmp['FACTOR'] = tmp['CANTIDAD_ESTUDIANTES'] * tmp[variable]
            grouped = tmp.groupby(['COLE_COD_MPIO_COLEGIO','MUNICIPIO'], as_index=False)[['FACTOR', 'CANTIDAD_ESTUDIANTES']].sum()
            grouped[variable] = grouped['FACTOR'] / grouped['CANTIDAD_ESTUDIANTES']

            grouped.rename(columns={variable: 'COUNT'},inplace=True)
            grouped.COLE_COD_MPIO_COLEGIO = grouped.COLE_COD_MPIO_COLEGIO.apply(lambda x: str(x).zfill(5))

            average = round(grouped.COUNT.mean(), 2)
            maximum = round(grouped.COUNT.max(), 2)
            minimum = round(grouped.COUNT.min(), 2)
            std = round(grouped.COUNT.std(), 2)
            if maximum < 1:
                annotations[0]['text']='<b>{} of <br>{}</b>'.format('percentage', variable)
            else:
                annotations[0]['text']='<b>{} of <br>{}</b>'.format('average', variable)
            figure = map_municipios(grouped)

    return figure, average, maximum, minimum, std