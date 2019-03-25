# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:20:41 2019

@author: SM Abdullah
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df_apple = pd.read_csv('AAPL.csv')
df_amazon = pd.read_csv('AMZN.csv')
df_google = pd.read_csv('GOOG.csv')


trace_apple = go.Scatter(
        x = df_apple['Date'],
        y = df_apple['High'],
        name = 'Apple Stock price',
        mode = 'lines',
        opacity = 0.8,
        line = {
                    'width':3,
                    'color': '#f4ad42'
                },
        marker = {
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                }
        )

trace_amazon = go.Scatter(
        x = df_amazon['Date'],
        y = df_amazon['High'],
        name = 'Amazon Stock price',
        mode = 'lines',
        opacity = 0.8,
        line = {
                    'width':3,
                    'color': '#42f4e2'
                },
        marker = {
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                }
        )

trace_google = go.Scatter(
        x = df_google['Date'],
        y = df_google['High'],
        name = 'Google Stock price',
        mode = 'lines',
        opacity = 0.8,
        line = {
                    'width':3,
                    'color': '#f4428c'
                },
        marker = {
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                }
        )


layout = go.Layout(
                xaxis={'type': 'date', 'title': 'Time'},
                yaxis={'title': 'High price'},
                margin={'l': 50, 'b': 40, 't': 40, 'r': 10},
                legend={'x': 0, 'y': 1, 'orientation':'h'},
                hovermode='closest',
                title = {
                        'text': 'Mar 25, 2015 to Mar 25, 2019 -- Stock Price Comparison'
                        }
            )

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [trace_apple, trace_amazon, trace_google],
            'layout': layout
        }
    )
])
    
if __name__ == '__main__':
    app.run_server(debug=True)

