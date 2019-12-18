
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.graph_objs import Layout

from components.filters import *
from components.summary_stats import *
from components.map import *

InfoColegios = pd.read_csv('data/clusters_Colegios.csv')

def build_segmentation():
    return [
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id="3dgraph", figure = build_segmentation_map())
                    ],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [
                        dcc.Graph(id="maps", figure = build_3Dgraph())
                    ],
                    className="pretty_container five columns",
                )
            ],
            className="row flex-display",
        )
    ]


def build_3Dgraph():
    layout = Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title='Segmentación Colegios',
        showlegend= False,
        scene = dict(
                    xaxis = dict(
                                title=dict(text='component 1'),
                                showticklabels=False,
                                showbackground=True,
                                visible=True),
                    yaxis = dict(
                                title=dict(text='component 2'),
                                showticklabels=False,
                                showbackground=True,
                                visible=True),
                    zaxis = dict(
                                title=dict(text='component 3'),
                                showticklabels=False,
                                showbackground=True,
                                visible=True))
    )
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=InfoColegios['PCA 1'],
                y=InfoColegios['PCA 2'],
                z=InfoColegios['PCA 3'],
                text=InfoColegios['COLE_NOMBRE'] + " - " + InfoColegios['COLE_MPIO_MUNICIPIO'],
                mode='markers',
                marker=dict(
                    size=3,
                    color=InfoColegios['Cluster'],                # set color to an array/list of desired values
                    colorscale='Portland',   # choose a colorscale
                    opacity=0.8
                )
            )
        ],
        layout = layout
    )
    camera = dict(
        eye=dict(x=0.8, y=0.8, z=0.8),
        up=dict(x=100, y=250, z=150)
    )
    fig.update_layout(scene_camera=camera)
    return fig


def build_segmentation_map():
    fig = go.Figure(go.Scattermapbox(lat=InfoColegios['LATITUD'], 
                                 lon=InfoColegios['LONGITUD'], 
                                 text=InfoColegios['COLE_NOMBRE'],
                                 marker=dict(
                                        size=9,
                                        color=InfoColegios['Cluster'],
                                        colorscale='Portland',
                                        opacity=0.6
                                 )))
    fig.update_layout(
        title='Nuclear Waste Sites on Campus',
        autosize=True,
        mapbox_style="carto-positron",
        mapbox_center_lon=-74.2973328,
        mapbox_center_lat=4.570868,
        mapbox_zoom=5
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig
