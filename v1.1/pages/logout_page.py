from dash import html
import dash
from helper_functions.custom_helpers import main_app

dash.register_page(__name__,path = main_app.environment_details['logout_page_link'])

layout = html.Div('Logging Out.....Please wait')