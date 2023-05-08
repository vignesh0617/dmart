import dash
from dash import  dcc,html, callback
import  dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
from helper_functions.custom_helpers import *
import plotly.express as px
import pandas as pd

dash.register_page(__name__,path=main_app.environment_details['dashboard_home_page_link'])

sample_data = px.data.gapminder()

right_side_nav_items = dbc.Nav([
    dbc.NavItem(dbc.NavLink("About",href = main_app.environment_details['about_page_link'],)),
    dbc.NavItem(dbc.NavLink("Logout",href = main_app.environment_details['logout_page_link'], id="logout"))
],className="ms-auto") 

left_side_nav_items = dbc.Nav([
    dbc.NavItem(dbc.NavLink("Dmart",href = "#"))
])

navbar = dbc.Navbar([
    left_side_nav_items,
    right_side_nav_items
],color = "#B0DAFF", className = "fw-bold")

row1 = dbc.Row([
    dbc.Col([
        navbar
    ])
])

row2 = dbc.Row([
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

page_layout = dbc.Card([
    row1,
    row2
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

# @callback(Output("token","clear_data"),Input("logout","n_clicks"))
# def logout_handler(n_clicks):
#     if(n_clicks is None):
#         raise PreventUpdate
#     return True

layout = html.Div([
    page_layout
])
