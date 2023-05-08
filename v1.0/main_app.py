from dash import Dash, html, dcc, callback
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import dash
from helper_functions.custom_helpers import *
import time

app = Dash(name = __name__,external_stylesheets=[dbc.themes.COSMO,dbc.icons.BOOTSTRAP],use_pages=True)

app.layout = html.Div([
    dcc.Location(id="url"),
    #the token is stored in local web browser for authenticating the user
    dcc.Store(id="token", storage_type = "session", data="") , 
    dash.page_container
    ])


@callback(Output("url","pathname"),Input("_pages_location","pathname"),State("token","data"))
def validate_token(pathname, token):
    try:
        payload = decode_token(token)
        session_not_over = payload['session_end_time'] > int(time.time())
        if session_not_over:
            if(pathname == "/"):
                return "/home"
            else:
                return pathname
        else:
            return "/"
    except Exception as e:
        print(f"Something Unexpected Happened inside link checks : {e}")
        return "/"


if(__name__ == "__main__"):
    app.run_server(port = 8051, debug = False)