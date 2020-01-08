# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load

# Imports from this application
from app import app

pipeline = load('assets/pipeline.pkl')

import pandas as pd

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
col1 = dbc.Col(
    [
        html.H2('Dinner Region Prediction', style={'textAlign': 'center'}),
        html.H5('Your dinner is most similar to Thanksgiving meals in the'),
        html.Div(id='prediction-content', className='mb-3', style={'textAlign': 'center', 'font-weight': 'bold',
                                                                   'font-color': 'blue'}),
        html.H5('region')
    ],

    md=4
)

col2 = dbc.Col(
    [
        # Pie Dropdown
        dcc.Markdown('##### What kind of pie did you have?'),
        dcc.Dropdown(
            id='pie',
            options=[
                {'label': 'Pumpkin', 'value': 'pumpkin'},
                {'label': 'Apple', 'value': 'apple'},
                {'label': 'Pecan', 'value': 'pecan'},
                {'label': 'Sweet Potato', 'value': 'sweet_potato'},
                {'label': 'Cherry', 'value': 'cherry'},
                {'label': 'Some other kind', 'value': 'other'},
                {'label': 'No pie', 'value': 'none'}

            ],
            multi=True,
            className='mb-3',
        ),
        # Cranberry Sauce Dropdown
        dcc.Markdown('##### What about cranberry sauce?'),
        dcc.Dropdown(
            id='cranberry_sauce',
            options=[
                {'label': 'Homemade', 'value': 'homemade'},
                {'label': 'Canned', 'value': 'canned'},
                {'label': 'None', 'value': 'none'},
                {'label': 'Both', 'value': 'both'}
            ],
            className='mb-3',
        ),
        # Vegetables Dropdown
        dcc.Markdown('##### What kind of vegetables did you have?'),
        dcc.Dropdown(
            id='vegetables',
            options=[
                {'label': 'Corn', 'value': 'corn'},
                {'label': 'Brussel Sprouts', 'value': 'brussel_sprouts'},
                {'label': 'Green Beans', 'value': 'green_beans'},
                {'label': 'Squash', 'value': 'squash'},
                {'label': 'Cauliflower', 'value': 'cauliflower'},
                {'label': 'None of these/no vegetables', 'value': 'none'}
            ],
            multi=True,
            className='mb-3',
        ),
        # Turkey cooking Dropdown
        dcc.Markdown('##### How was your turkey cooked?'),
        dcc.Dropdown(
            id='main_dish_cooked',
            options=[
                {'label': 'Oven roasted', 'value': 'roasted'},
                {'label': 'Deep fried', 'value': 'fried'},
                {'label': 'Smoked', 'value': 'smoked'},
                {'label': 'We didn\'t have turkey', 'value': 'no_turkey'}
            ],
            className='mb-3',
        ),
        # Rolls/Biscuits Dropdown
        dcc.Markdown('##### Were there rolls and/or biscuits on the table?'),
        dcc.Dropdown(
            id='rolls',
            options=[
                {'label': 'No', 'value': 'No'},
                {'label': 'Yes', 'value': 'Yes'},
            ],
            className='mb-3',
        ),
        # Mac and Cheese Dropdown
        dcc.Markdown('##### Was macaroni and cheese one of the dishes?'),
        dcc.Dropdown(
            id='mac_n_cheese',
            options=[
                {'label': 'No - who eats that on Thanksgiving?', 'value': 'No'},
                {'label': 'Yes', 'value': 'Yes'},
            ],
            className='mb-3',
        ),
        # Potatoes Dropdown
        dcc.Markdown('##### Did you serve mashed potatoes?'),
        dcc.Dropdown(
            id='mashed_potatoes',
            options=[
                {'label': 'No', 'value': 'No'},
                {'label': 'Of course!', 'value': 'Yes'},
            ],
            className='mb-3',
        ),
        # Sweet Potatoes Dropdown
        dcc.Markdown('##### How about sweet potatoes?'),
        dcc.Dropdown(
            id='sweet_potatoes',
            options=[
                {'label': 'No', 'value': 'No'},
                {'label': 'Yes', 'value': 'Yes'},
            ],
            className='mb-3',
        ),
        # Cornbread Dropdown
        dcc.Markdown('##### Did you have cornbread?'),
        dcc.Dropdown(
            id='cornbread',
            options=[
                {'label': 'No', 'value': 'No'},
                {'label': 'Yes', 'value': 'Yes'},
            ],
            className='mb-3',
        ),

    ],

)


@app.callback(
    Output('prediction-content', 'children'),
    [
        Input('pie', 'value'),
        Input('cranberry_sauce', 'value'),
        Input('vegetables', 'value'),
        Input('main_dish_cooked', 'value'),
        Input('rolls', 'value'),
        Input('mac_n_cheese', 'value'),
        Input('mashed_potatoes', 'value'),
        Input('sweet_potatoes', 'value'),
        Input('cornbread', 'value'),
    ]
)

#function to reformat data and create prediction
def predict(pie, cranberry_sauce, vegetables, main_dish_cooked, rolls, mac_n_cheese,
            mashed_potatoes, sweet_potatoes, cornbread):
    # initial assignment of all variables to 'No'
    pumpkin_pie = homemade_cranberry = corn = green_beans = apple_pie = squash = \
        brussel_sprouts = cherry_pie = sweet_potato_pie = pecan_pie = canned_cranberry = cauliflower = \
        roasted_turkey = fried_turkey = 'No'
    for value in pie:
        if value is 'pumpkin':
            pumpkin_pie = 'Yes'
        elif value is 'apple':
            apple_pie = 'Yes'
        elif value is 'pecan':
            pecan_pie = 'Yes'
        elif value is 'sweet_potato':
            sweet_potato_pie = 'Yes'
        elif value is 'cherry':
            cherry_pie = 'Yes'
    for value in vegetables:
        if value is 'corn':
            corn = 'Yes'
        elif value is 'green_beans':
            green_beans = 'Yes'
        elif value is 'squash':
            squash = 'Yes'
        elif value is 'brussel_sprouts':
            brussel_sprouts = 'Yes'
        elif value is 'cauliflower':
            cauliflower = 'Yes'

    for value in main_dish_cooked:
        if value is 'roasted':
            roasted_turkey = 'Yes'
        elif value is 'fried':
            fried_turkey = 'Yes'
    for value in cranberry_sauce:
        if value is 'homemade':
            homemade_cranberry = 'Yes'
        if value is 'canned':
            canned_cranberry = 'Yes'
        if value is 'both':
            homemade_cranberry = 'Yes'
            canned_cranberry = 'Yes'

    input_df = pd.DataFrame(
        columns=['Pumpkin_Pie', 'Homemade_Cranberry_Sauce', 'Corn', 'Rolls_Biscuits', 'Green_Beans',
                 'Apple_Pie', 'Squash', 'Mac_and_Cheese', 'Mashed_Potatoes', 'Brussel_Sprouts', 'Cornbread',
                 'Sweet_Potatoes',
                 'Cherry_Pie', 'Sweet_Potato_Pie', 'Pecan_Pie', 'Canned_Cranberry_Sauce', 'Cauliflower', 'Roast_Turkey',
                 'Fried_Turkey'],
        data=[[pumpkin_pie, homemade_cranberry, corn, rolls, green_beans,
               apple_pie, squash, mac_n_cheese, mashed_potatoes, brussel_sprouts, cornbread, sweet_potatoes,
               cherry_pie, sweet_potato_pie, pecan_pie, canned_cranberry, cauliflower, roasted_turkey, fried_turkey]]
    )
    y_pred = pipeline.predict(input_df)[0]
    return y_pred


col2_title = dbc.Row([html.H2('What foods were in your meal?', className='mb-6')], className='mb-3')
layout = dbc.Row([col1, col2])
