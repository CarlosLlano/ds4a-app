import dash_core_components as dcc
import dash_html_components as html
from controls import PERIODS


def periods_slider():
    return dcc.RangeSlider(
            id="year_slider",
            min=0,
            max=21,
            value=[0, 21],
            className="dcc_control",
        )


def periods_slider_dashboard_detailed():
    return dcc.RangeSlider(
            id="year_slider_dashboard_detailed",
            min=0,
            max=21,
            value=[0, 21],
            className="dcc_control",
        )