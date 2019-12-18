
import dash_core_components as dcc
import dash_html_components as html

from components.dashboard import *
from components.simulator import *
from components.segmentation import *

def build_tabs():
    return dcc.Tabs(
        id="tabs",
        value='Dashboard',
        children=[
            dcc.Tab(label='Dashboard', value='Dashboard'),
            dcc.Tab(label='Simulator', value='Simulator'),
            dcc.Tab(label='Segmentation', value='Segmentation')
        ],
        colors={
            "border": "white",
            "primary": "white",
            "background": "Gainsboro"
        }
    )

def build_content_for_tab(tab_name):
    if tab_name == 'Dashboard':
        return build_dashboard()
    elif tab_name == 'Simulator':
        return build_simulator()
    elif tab_name == 'Segmentation':
        return build_segmentation()