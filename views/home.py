
from app import app, server

import dash
import requests
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from pandas.io.json import json_normalize
import json
from flask import session
from flask_login import current_user
from group_assessment.assessment import GroupAssessment
from group_overall_progress.overall_progress import GroupOverallProgress
from group_planning.planning import GroupPlanning

dash.register_page(__name__,
                   path='/overall_progress',
                   name='Overall progress',
                   title='Overall progress')




# try:
#     r = requests.get('http://127.0.0.1:8050/data')
#     print(r)
# except ConnectionError:
#     print('ok')

# r = requests.get('http://localhost:5000/api/users')

# # This is the JSON object, that you can use to populate your visualizations with data :)
# data = r.json()
# df2 = json_normalize(data['result']) 
# # df = pd.DataFrame.from_dict(data['result'], orient='index')
# # df = df.transpose()
# # print(df2.head())
# df2 = df2[['id', 'username', 'email' ,'password']]

# layout = dash_table.DataTable(df2.to_dict('records'), [{"id": i, "name": i} for i in df2.columns],
# style_data={
#         'color': 'black',
#         'backgroundColor': 'white'
#     },
#     style_data_conditional=[
#         {
#             'if': {'row_index': 'odd'},
#             'backgroundColor': 'rgb(220, 220, 220)',
#         }
#     ],
#     style_header={
#         'backgroundColor': 'rgb(210, 210, 210)',
#         'color': 'black',
#         'fontWeight': 'bold'
#     })


###############################################################################
########### LANDING PAGE LAYOUT ###########
###############################################################################
layout = dbc.Container([

        html.H2('Homepage Layout'),
        html.Hr(),
        html.Img(src='/assets/Mobile-M-Icon-1-corners.png', className="ml-auto", style={'height':'8%', 'width':'8%'}),


], className="mt-4")
