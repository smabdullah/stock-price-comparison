# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:20:41 2019

@author: SM Abdullah
"""
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#app = dash.Dash(__name__)

server = app.server

# reading data from the csv files
df_apple = pd.read_csv('AAPL.csv')
df_amazon = pd.read_csv('AMZN.csv')
df_google = pd.read_csv('GOOG.csv')

# converting the 'Date' column to pandas datetime to extract year
df_apple['Date'] = pd.to_datetime(df_apple['Date'])
df_amazon['Date'] = pd.to_datetime(df_amazon['Date'])
df_google['Date'] = pd.to_datetime(df_google['Date'])

# add a new column 'Year' to each data frame
df_apple['Year'] = df_apple['Date'].dt.year
df_amazon['Year'] = df_amazon['Date'].dt.year
df_google['Year'] = df_google['Date'].dt.year

company_name = ['Apple', 'Amazon', 'Google']
company_df = [df_apple, df_amazon, df_google]
color = ['#f4ad42', '#42f4d9', '#8042f4']
columns = ['','Open','High','Low','Close','Adj close']

app.layout = html.Div([
    html.Div([html.H1('A web-based Python visulasition for historical stock data'),
              html.P('The following scatter plot displays different prices (open, close and others) based on the user\'s choice')
            ], style = {'margin-left': '10px'}),

    html.Div([html.Label(['Choose a price comparison indicator'], style = {'font-weight': 'bold'}),
            dcc.RadioItems(id = 'radio_stock',
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
    ], style = {'margin-left': '10px'}),
            
    html.Div([dcc.Graph(id='stock_price')]),
    
    html.Div([html.P('The following bar-chart displays the volume of sale in a particular year')
            ], style = {'margin-left': '10px'}),
    
    html.Div([
            html.Label(['Choose a year'], style = {'font-weight': 'bold'}),
            dcc.RadioItems(
                    id = 'volume_year',
                    options=[
                            {'label': '2015', 'value': 2015},
                            {'label': '2016', 'value': 2016},
                            {'label': '2017', 'value': 2017},
                            {'label': '2018', 'value': 2018},
                            {'label': '2019', 'value': 2019}
                    ],
                    value=2018,
                    labelStyle = {'display': 'inline-block'}
            )
    ], style = {'margin-left': '10px'}),
    
    html.Div([dcc.Graph(id = 'bar_chart')
            
    ])
], style = {'background-color': 'lightGray'})

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
                    legend={'x': 0, 'y': 1, 'orientation':'h', 'bgcolor': 'rgba(255,0,0,0)'},
                    hovermode='closest',
                    plot_bgcolor='lavender'
            )
    }
    
@app.callback(
        Output('bar_chart', 'figure'),
        [Input('volume_year', 'value')])
def update_bar(year):
    bar_trace = []
    for i in range(len(company_name)):
        bar_trace.append(go.Bar(
                    x = company_df[i].loc[company_df[i]['Year'] == year, 'Date'],
                    y = company_df[i].loc[company_df[i]['Year'] == year, 'Volume'],
                    name = '{}'.format(company_name[i]),
                    opacity = 0.8,
                    marker = {'color': color[i]}
            )                    
    )
    
    return {
        'data': bar_trace,
        'layout': go.Layout(
                    barmode = 'group',
                    xaxis = {'type': 'date', 'title': 'Time in year'},
                    yaxis = {'type': 'log', 'title': 'Volume in log scale'},
                    legend={'x': 0, 'y': 1, 'orientation':'h', 'bgcolor': 'rgba(255,0,0,0)'},
                    margin = {'l': 50, 'b': 40, 't': 40, 'r': 10},
                    hovermode = 'closest',
                    plot_bgcolor='lavender'
                )        
    }
    
# external stylesheet (css)
'''external_css = ["https://fonts.googleapis.com/icon?family=Material+Icons", "https://code.getmdl.io/1.3.0/material.indigo-pink.min.css"]
for css in external_css:
    app.css.append_css({'external_url': css})
    
# external javascript file
external_js = ["https://code.getmdl.io/1.3.0/material.min.js"]
for js in external_js:
    app.scripts.append_script({'external_url': js})'''

if __name__ == '__main__':
    app.run_server(debug=True)

