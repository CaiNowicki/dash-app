import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

import pandas as pd


df = pd.read_csv('assets/wrangled_data.csv')

#create plotly express visualizations
figure1 = px.density_heatmap(df, x='Mac_and_Cheese', y='Type_of_Thanksgiving', hover_data=df.columns,
                             title='Mac and Cheese Heatmap', width=400, height=400)
figure1.update_xaxes(title_text='Was Mac and Cheese Served?', automargin=True)
figure1.update_yaxes(title_text='Thanksgiving Regional Type', automargin=True)

figure2 = px.density_heatmap(df, x='Mac_and_Cheese', y='Type_of_Thanksgiving', hover_data=df.columns,
                             histnorm='percent', title='Mac and Cheese Percentage Heatmap', width=400, height=400)
figure2.update_xaxes(title_text='Was Mac and Cheese Served?', automargin=True)
figure2.update_yaxes(title_text='Thanksgiving Regional Type', automargin=True)

figure3 = px.histogram(df, x='Main_Dish', y='Type_of_Thanksgiving', title='Main Dish Types', width=400, height=400)
figure3.update_xaxes(title_text='Main Dish', automargin=True)
figure3.update_yaxes(title_text='Total Count', automargin=True)


column1 = dbc.Col(
    [
        dcc.Markdown(
            """

           ## Data Visualizations 

           It's often easier to understand the relationship between factors in data by using visualizations. 
           
           One of the steps necessary in creating a model which is efficient as well as accurate is determining which features matter the most when training the model. There are several ways which this can be done. 
           
           This visualization is called a heat map. It shows the relationship between two variables and lets you 
           see how many items fall into each group for both variables.

           """
        ),
        dcc.Graph(figure=figure1),
        html.Br(),
        html.Br(),
        dcc.Markdown(
            """Sometimes, a visualization can show you a lack of relationship, too, which is also useful. For 
            example, this graph shows that an overwhelming percentage of poll-takers unsurprisingly had turkey 
            regardless of region, and so few of them had anything else that it was not a useful feature for 
            determining regional preferences """
        ),
        html.Br(),
        dcc.Graph(figure=figure3)
    ],
    md=4,
)
column2 = dbc.Col(
    [
        html.Br(),
        html.Br(),
        dcc.Markdown(
            """

           Alternatively, you can use the same figure to show relative percentages instead of total count. 
           
           With this visualization, you can see that while there are many more responses for diners who didn't have 
           macaroni and cheese, those who did were more likely to be in the southeast. That made it an important 
           feature to include in training my model. 

           """
        ),
        dcc.Graph(figure=figure2),
        html.Br(),
        dcc.Markdown(
            """
            
            Graphics like these have one major limitation - they only allow you the explore the relationship between 
            a few variables at a time. That's not very efficient when dealing with a dataset where there are many 
            columns. This dataset initially had 65 columns, and I ended up with 47 columns for different dishes and 
            cooking methods. I wouldn't want to sit there and compare each of those against my target using a heat 
            map or histogram! 
            
            Instead, you can use permutation importance, which is a method to show how important all of your 
            variables are to the model at the same time. 
            
            """
            ),
        html.Img('assets/feature_importance.png'),
        
    ],
    md=4,
)
layout = dbc.Row([column1, column2])