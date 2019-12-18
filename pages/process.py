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
        
            ## Process

            This was a surprisingly difficult project. It took quite a bit of work to create a model that had a reasonable level of accuracy. 

            I was surprised at the features that ended up impacting the model the most. Having whether or not someone was a Black Friday shopper affect the region, for example, was something I did not expect.
            """
        ),

    ],
)

layout = dbc.Row([column1])