# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/cereal.csv')

# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Scatter Plot'),

    # set the description underneath the heading
    html.Div(children='''
        Exercise 2 scatter plot for cereal data.
    '''),

# append the visualization to the page
    dcc.Graph(
        id='Cereal',
        figure={
            # configure the data
            'data': [
                go.Scatter(
                    x=df['calories'],
                    y=df['sodium'],
                    mode='markers',
                    text=df['calories'],
                    marker={
                        'size': 10,
                        'opacity': 0.6,
                        'color': "orange",
                    }
                )
            ],
            'layout': {
                'title': 'Cereal Scatter Plot',
                # It is always a good practice to have axis labels.
                # This is especially important in this case as the numbers are not trivial
                'xaxis': {'title': 'Calories'},
                'yaxis': {'title': 'Amount of salt (sodium)'},
            }
        }
    )

])



if __name__ == '__main__':
    app.run_server(debug=True)