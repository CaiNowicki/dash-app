import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

import pandas as pd

df = pd.read_csv('assets/wrangled_data.csv')
figure1 = px.density_heatmap(df, x='Mac_and_Cheese', y='Type_of_Thanksgiving', hover_data=df.columns)
figure1.update_xaxes(title_text='Was Mac and Cheese Served?')
figure1.update_yaxes(title_text='Thanksgiving Regional Type')

df = pd.read_csv('assets/wrangled_data.csv')
figure2 = px.density_heatmap(df, x='Mac_and_Cheese', y='Type_of_Thanksgiving', hover_data=df.columns, histnorm='percent')
figure2.update_xaxes(title_text='Was Mac and Cheese Served?')
figure2.update_yaxes(title_text='Thanksgiving Regional Type')

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
        dcc.Graph(figure=figure1),
    ],
    md=4,
)
column2 = dbc.Col(
    [
        dcc.Markdown(
            """

           Alternatively, you can use the same figure to show relative percentages instead of total count. 

           """
        ),
        dcc.Graph(figure=figure2),
    ],
    md=4,
)
layout = dbc.Row([column1, column2])