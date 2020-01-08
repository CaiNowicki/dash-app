import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

import pandas as pd

df = pd.read_csv('assets/wrangled_data.csv')
figure = px.density_heatmap(df, x='Mac_and_Cheese', y='Type_of_Thanksgiving', hover_data=df.columns)
figure.update_xaxes = 'Was Mac and Cheese Served?'
figure.update_yaxes = 'Thanksgiving Regional Type'

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

           ## Data Visualizations 

           It's often easier to understand the relationship between factors in data by using visualizations.
           
           This visualization is called a heat map. It shows the relationship between two variables and lets you 
           see how many items fall into each group for both variables. 

           """
        ),
        dcc.Graph(figure=figure)
    ],
    md=4,
)

layout = dbc.Row([column1])