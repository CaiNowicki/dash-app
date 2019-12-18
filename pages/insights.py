# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            I had to do a lot of feature engineering to get these results! The data by itself wasn't all that informative, so I had to combine it in order to create useful features.


            """
        ),

    ],
)

layout = dbc.Row([column1])
