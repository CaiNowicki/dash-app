# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
col1 = dbc.Col(
     [
        html.H2('Dinner Region Prediction', style={'textAlign': 'center'}),
    ],
    
    md = 4
)

col2 = dbc.Col(    
    [
     # Pie Dropdown
        dcc.Markdown('##### What kind of pie did you have?'),
        dcc.Dropdown(
            id='pie', 
            options= [
                {'label': 'Pumpkin', 'value': 'pumpkin'},
                {'label': 'Apple', 'value': 'apple'},
                {'label': 'Pecan', 'value': 'pecan'},
                {'label': 'Sweet Potato', 'value': 'sweet_potato'},
                {'label': 'Cherry', 'value': 'cherry'}
                
            ],
            multi=True,
            className = 'mb-3',
        ),
        # Cranberry Sauce Dropdown
        dcc.Markdown('##### What about cranberry sauce?'),
        dcc.Dropdown(
            id='cranberry_sauce', 
            options= [
                {'label': 'Homemade', 'value': 'homemade'},
                {'label': 'Canned', 'value': 'canned'},
                {'label': 'None', 'value': 'none'}
            ],
            className = 'mb-3',
        ),
        # Vegetables Dropdown
        dcc.Markdown('##### What kind of vegetables did you have?'),
        dcc.Dropdown(
            id='vegetables', 
            options= [
                {'label': 'Corn', 'value': 'corn'},
                {'label': 'Brussel Sprouts', 'value': 'brussel_sprouts'},
                {'label': 'Green Beans', 'value': 'green_beans'},
                {'label': 'Squash', 'value': 'squash'}
                {'label': 'Cauliflower', 'value': 'cauliflower'}
                {'label': 'None of these/no vegetables', 'value': 'none'}
            ],
            multi=True,
            className = 'mb-3',
        ),
    # Turkey cooking Dropdown
        dcc.Markdown('##### How was your turkey cooked?'),
        dcc.Dropdown(
            id='main_dish_cooked', 
            options= [
                {'label': 'Oven roasted', 'value': 'roasted},
                {'label': 'Deep fried', 'value': 'fried'},
                {'label': 'Smoked', 'value': 'smoked'},
                {'label': 'We didn\'t have turkey', 'value': 'no_turkey'} 
            ],
            className = 'mb-3',
        ), 
        # Rolls/Biscuits Dropdown
        dcc.Markdown('##### Were there rolls and/or biscuits on the table?'),
        dcc.Dropdown(
            id='rolls', 
            options= [
                {'label': 'No', 'value': 0},
                {'label': 'Yes', 'value': 1},
            ],
            className = 'mb-3',
        ),
        # Mac and Cheese Dropdown
        dcc.Markdown('##### Was macaroni and cheese one of the dishes?'),
        dcc.Dropdown(
            id='mac_n_cheese', 
            options= [
                {'label': 'No - who eats that on Thanksgiving?', 'value': 0},
                {'label': 'Yes', 'value': 1},
            ],
            className = 'mb-3',
        ),
        # Potatoes Dropdown
        dcc.Markdown('##### Did you serve mashed potatoes?'),
        dcc.Dropdown(
            id='mashed_potatoes', 
            options= [
                {'label': 'No', 'value': 0},
                {'label': 'Of course!', 'value': 1},
            ],
            className = 'mb-3',
        ),
        # Sweet Potatoes Dropdown
        dcc.Markdown('##### How about sweet potatoes?'),
        dcc.Dropdown(
            id='sweet_potatoes', 
            options= [
                {'label': 'No', 'value': 0},
                {'label': 'Yes', 'value': 1},
            ],
            className = 'mb-3',
        ),
        # Cornbread Dropdown
        dcc.Markdown('##### Did you have cornbread?'),
        dcc.Dropdown(
            id='cornbread', 
            options= [
                {'label': 'No', 'value': 0},
                {'label': 'Yes', 'value': 1},
            ],
            className = 'mb-3',
         ),
        
        
    ],
   
    
)

layout = dbc.Row([col1, col2])
