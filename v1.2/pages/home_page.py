import dash
from dash import  dcc,html, callback
import  dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
from helper_functions.custom_helpers import *
import plotly.express as px
import pandas as pd
from components.navbar import navbar

sample_data = px.data.gapminder()


body = dbc.Row([
    dbc.Col([
        "Filters : ",
        dcc.Dropdown( id ="continent_filter",
                        options = sample_data['continent'].sort_values().unique(),
                        value = sample_data['continent'].sort_values().unique()[0]),
        html.Br(),
        dcc.Dropdown(id = "year_filter",
                        options = sample_data['year'].sort_values().unique(),
                        value = sample_data['year'].sort_values().unique()[0])
        
    ],width = 3 , className = "border"),
    dbc.Col([
        html.H1("Graphs"),
        dbc.Spinner(dcc.Graph(id="graph_output"))
    ],width = 9 , className = "border")
],className="h-100")

page_layout = html.Div([
    navbar,
    body
],className = "vh-100")


@callback(Output("graph_output","figure"),Input("continent_filter","value"),Input("year_filter","value"))
def bar_graph(continent,year):
    if continent is None or year is None :
        raise PreventUpdate
    bar = px.bar(data_frame = sample_data.query("continent == @continent and year == @year"),
          x = 'country',
          y = 'pop',
          title = f"Population in {continent}  Continent in Year : {year}")
    return bar

# @callback(Output("url2","pathname"),Input("logout","n_clicks"))
# def logout_handler(n_clicks):
#     if(n_clicks is None):
#         raise PreventUpdate
#     return main_app.environment_details['home_page_link']

# @callback(Output("url2","pathname"),Input("main_page_url","pathname"))
# def update_url(pathname):
#     print(f'executing this function -----> {pathname}')
#     return pathname

layout = html.Div([
    page_layout
])
