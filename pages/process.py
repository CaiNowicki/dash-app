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

            The data for this app came from a poll on the news site FiveThirtyEight and is available on their GitHub. 
            
            In the process of creating this quiz, I had to change my goals a few times in order to create something 
            that would work. Originally I wanted to create a quiz that would predict where the user was from based on 
            their Thanksgiving dinner, but I wasn't able to create an accurate model based on the available data. I 
            think this shows that American traditions tend to move with families, and many Americans are more mobile 
            than we used to be. 
            
            Instead, I decided to create this quiz, which is more about the food than the user. It ended up requiring 
            a fair amount of research to create groups of traditional Thanksgiving dishes that are either specific to 
            or significantly more prevalent in particular regions of the country. 
            
            It was also a bit tricky to decide what constitutes a "region"! For example, is Pennsylvania part of the 
            Northeast? What about Ohio? Is Arkansas southern or midwest? Where do Hawaii and Alaska fall? I ended up 
            making most of the distinctions based on what I could find on the popular foods there, and if I wasn't 
            sure what region something went into, I decided based on which region had the most other similar dishes. 
            I also didn't want to create too many different regions if there weren't obvious differences in 
            Thanksgiving traditions between them 
            
            I chose to give Hawaii its own region because there are regional dishes popular there 
            which are entirely absent on Thanksgiving tables in the rest of the country, such as smoked turkey and 
            fresh fish. However, none of the initial poll data ended up coming out as the Hawaiian region, 
            so I wasn't able to use my model to predict that region. In the end, I had to leave it out since it 
            wasn't actually possible to get that region as a result. 
            
            This problem is considered "classification", because I'm trying to put a specific data point (in this 
            case, your Thanksgiving dinner) into a class. A regression problem is one where I would be trying to 
            predict a numerical value based on past values, such a predicting the rent cost of an apartment. However, 
            I ended up using a logistic regression model (which predicts the probability that a data point falls into 
            each class) rather than a "true" classification model (which just assigns a class to each data point) as 
            the logistic regression model was more accurate. 


            """
        ),

    ],
)

layout = dbc.Row([column1])