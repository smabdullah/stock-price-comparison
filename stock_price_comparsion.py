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

company_name = ['Apple', 'Amazon', 'Google']
company_df = [df_apple, df_amazon, df_google]
color = ['#f4ad42', '#42f4d9', '#8042f4']

app.layout = html.Div([
    html.Div([
            html.Label('Price comparison indicator'),
            dcc.RadioItems(
                    options=[
                            {'label': 'Open', 'value': 0},
                            {'label': 'High', 'value': 1},
                            {'label': 'Low', 'value': 2},
                            {'label': 'Close', 'value': 3},
                            {'label': 'Adj close', 'value': 4}
                    ],
                    value=3,
                    labelStyle = {'display': 'inline-block'}
            )
    ]),
    html.Div([
            dcc.Graph(
                    id='stock-price',
                    figure={
                            'data': [go.Scatter(
                                x = company_df[i]['Date'],
                                y = company_df[i]['High'],
                                name = '{} Stock price'.format(company_name[i]),
                                mode = 'lines',
                                opacity = 0.8,
                                line = {
                                        'width':3,
                                        'color': color[i]
                                        },
                                marker = {
                                        'size': 15,
                                        'line': {'width': 0.5, 'color': 'white'}
                                        }
                                )for i in range(len(company_name))
                        ],
                            'layout': go.Layout(
                                xaxis={'type': 'date', 'title': 'Time'},
                                yaxis={'title': 'High price'},
                                margin={'l': 50, 'b': 40, 't': 40, 'r': 10},
                                legend={'x': 0, 'y': 1, 'orientation':'h'},
                                hovermode='closest',
                                title = {
                                            'text': 'Mar 25, 2015 to Mar 25, 2019 -- Stock Price Comparison'
                                        }
                                )
                        }
                    )
            ])
])
    
if __name__ == '__main__':
    app.run_server(debug=True)

