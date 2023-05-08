import dash
from dash import  html, callback
import  dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
from helper_functions.custom_helpers import *
import pandas as pd

dash.register_page(__name__,path="/home")

layout = html.Div([
    "This is the home page",
    dbc.Button("Test", id ="sample-2"),
    html.Div(id="sample-output")
])

@callback(Output("sample-output","children"),Input("sample-2","n_clicks"))
def test2(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    data = pd.read_sql("select * from pythonautomation.adrc", main_app.connector)
    print(data)
    return "Working ??"