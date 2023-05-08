from importlib.resources import path
from json.tool import main
from dash import Dash, html, dcc, callback
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import dash
from helper_functions.custom_helpers import *
import time
from flask import Flask, request, redirect, session

c=0
server = Flask(__name__)
app = Dash(name = __name__,external_stylesheets=[dbc.themes.COSMO,dbc.icons.BOOTSTRAP],use_pages=True , 
            server = server)

# @app.server.route("/")
# @app.server.route("/<any_url>/<path:path>")
# def validate_token(any_url ="",path =""):
#     print("----------------------executing-----------------")
#     try:
#         payload = decode_token(session.get("token"))
#         pathname = any_url+"/"+path
#         session_not_over = payload['session_end_time'] > int(time.time())
#         if session_not_over:
#             # if(any_url == "login"):
#             return dash.page_registry.get('pages.home_page')['layout']
#             # else:
#             #     return redirect(pathname)
#         else:
#             return redirect("/")
#     except Exception as e:
#         print(f"Something Unexpected Happened inside link checks : {e}")
#         return redirect("/")

# app.server.add_url_rule(view_func=)
# app.server.before_request(pre_render_function)


app.layout = html.Div([
    dcc.Location(id="url"),
    #the token is stored in local web browser for authenticating the user
    dcc.Store(id="token", storage_type = "session", data="") , 
    dash.page_container
    ])


@callback(Output("url","pathname"),Output("token","clear_data"),Input("_pages_location","pathname"),State("token","data"))
def validate_token(pathname, token):
    global c
    c+=1
    print(f'count number {c} ----- pathname >>>>>>>> {pathname} ')
    try:
        payload = decode_token(token)
        session_not_over = payload['session_end_time'] > int(time.time())
        if session_not_over:
            if(pathname == main_app.environment_details['login_page_link']):
                print("1.1--------------------")
                return main_app.environment_details['dashboard_home_page_link'],False
            elif(pathname == main_app.environment_details['logout_page_link']):
                print("1.2--------------------")
                main_app.connector = ""
                return main_app.environment_details['login_page_link'],True
            else:
                print("1.3--------------------")
                return pathname,False
        else:
            print("1.4--------------------")
            return main_app.environment_details['login_page_link'],False
    except Exception as e:
        print(f"Something Unexpected Happened inside link checks : {e}")
        print("1.5--------------------")
        return main_app.environment_details['login_page_link'],False


if(__name__ == "__main__"):
    app.run_server(port = 8051, debug = False)