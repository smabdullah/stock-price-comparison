# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:20:41 2019

@author: SM Abdullah
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
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
columns = ['','Open','High','Low','Close','Adj close']

bar_trace = []

for i in range(len(company_name)):
    bar_trace.append(go.Bar(
                    x = company_df[i]['Date'],
                    y = company_df[i]['Volume'],
                    name = '{}'.format(company_name[i])
            )                    
    )

app.layout = html.Div([
    html.Div([
            html.Label('Price comparison indicator'),
            dcc.RadioItems(
                    id = 'radio_stock',
                    options=[
                            {'label': 'Open', 'value': 1},
                            {'label': 'High', 'value': 2},
                            {'label': 'Low', 'value': 3},
                            {'label': 'Close', 'value': 4},
                            {'label': 'Adj close', 'value': 5}
                    ],
                    value=4,
                    labelStyle = {'display': 'inline-block'}
            )
    ]),
            
    html.Div([dcc.Graph(id='stock_price')]),
    
    html.Div([dcc.Graph(
                id = 'bar_chart',
                figure = {
                    'data': bar_trace,
                    'layout': go.Layout(
                            barmode = 'group'
                    )
                }
            )
            
    ])
])

@app.callback(
        Output('stock_price', 'figure'),
        [Input('radio_stock', 'value')])
def update_figure(df_index):
    trace = []
    for i in range(len(company_name)):
        trace.append(go.Scatter(
            x = company_df[i]['Date'],
            y = company_df[i].iloc[:, df_index],
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
            )
    ) 
    
    return {
            'data': trace,
            'layout': go.Layout(
                    xaxis={'type': 'date', 'title': 'Time'},
                    yaxis={'title': '{} price'.format(columns[df_index])},
                    margin={'l': 50, 'b': 40, 't': 40, 'r': 10},
                    legend={'x': 0, 'y': 1, 'orientation':'h'},
                    hovermode='closest'
            )
    }

if __name__ == '__main__':
    app.run_server(debug=True)

