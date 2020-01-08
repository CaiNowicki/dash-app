# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
             """
        
            ## Thanksgiving Quiz! What region are your family's Thanksgiving foods from? This quiz will ask you about 
            a few of the foods you eat at Thanksgiving and tell you what region of the country your dinner is most 
            similar to. The regional options are Californian/Pacific Coast, New England, middle America/Midwest, 
            and Southeast. 
            
            """
        ),
        dcc.Link(dbc.Button('Take the Quiz Now!', color='primary'), href='/predictions')
    ],
    md=4,
)


layout = dbc.Row([column1])
