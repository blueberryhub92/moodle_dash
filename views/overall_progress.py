import json
from group_overall_progress.overall_progress import GroupOverallProgress
from flask import jsonify, session, url_for
import dash
import pandas as pd
import requests
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from app import app, server

dash.register_page(__name__,
                   path='/overall_progress',
                   name='Overall progress',
                   title='Overall progress')

layout = html.Div([
    html.Div(id='output-div')
])

@app.server.route('/api/group/overall_progress')
def get_overall_progress():
    user = session.get('user')
    instance_of_overall_progress = GroupOverallProgress(app=server, user=user)
    return instance_of_overall_progress.operation()

@app.callback(
    dash.dependencies.Output('output-div', 'children'),
    [dash.dependencies.Input('url', 'pathname')])
def update_output(pathname):
    if pathname is None:
        return "Wait for the page to load"
    else:
        url = 'http://localhost:8050/api/group/overall_progress'
        response = requests.get(url)
        data = response.json()
        user_all_activities = pd.read_json(data[0])
        unseen = pd.read_json(data[1])
        perc = pd.read_json(data[2])
        # print(user_all_activities)

        # getting the percentages from the perc df
        quiz_perc = perc[0][0]
        assignment_perc = perc[0][1]
        url_perc = perc[0][2]
        file_perc = perc[0][3]
        
        fig4 = go.Figure(data=[go.Table(
                    header=dict(values=['<b> Completed</b>', '<b>Not Completed</b>'],
                                fill_color='paleturquoise',
                                align='left'),
                    cells=dict(values=[user_all_activities[user_all_activities['Component'] == "Quiz"]['Event context'],
                                       unseen[unseen['Component'] == "Quiz"]['Event context']],
                               fill_color='lavender',
                               align='left'))

                                            ])
        fig4.update_layout(width=550, height=250, autosize=False, margin=dict(l=10, r=25, b=5, t=5))

        fig5 = go.Figure(data=[go.Table(
            header=dict(values=['<b> Completed</b>', '<b>Not Completed</b>'],
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[user_all_activities[user_all_activities['Component'] == "Assignment"]['Event context'],
                               unseen[unseen['Component'] == "Assignment"]['Event context']],
                       fill_color='lavender',align='left'))

        ])
        fig5.update_layout(width=550, height=250, autosize=False, margin=dict(l=15, r=15, b=5, t=5))

        fig6 = go.Figure(data=[go.Table(
            header=dict(values=['<b> Seen</b>', '<b>Not Seen</b>'],
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[user_all_activities[user_all_activities['Component'] == "URL"]['Event context'],
                               unseen[unseen['Component'] == "URL"]['Event context']],
                       fill_color='lavender',
                       align='left'))

        ])
        fig6.update_layout(width=550, height=250, autosize=False, margin=dict(l=15, r=25, b=5, t=5))
        fig7 = go.Figure(data=[go.Table(
            header=dict(values=['<b> Seen</b>', '<b>Not Seen</b>'],
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[user_all_activities[user_all_activities['Component'] == "File"]['Event context'],
                               unseen[unseen['Component'] == "File"]['Event context']],
                       fill_color='lavender',
                       align='left'))

        ])
        fig7.update_layout(width=550, height=250, autosize=False, margin=dict(l=15, r=15, b=5, t=5))

        return dbc.Container([
                dbc.Row([
                    dbc.Col([html.H3("Quiz",style={'margin-left':'15px'}),
                            dbc.Progress(label=quiz_perc, value=quiz_perc, max=100, striped=True, color="success",
                                        style={'hight': '20px','margin-left' :'20px'}), html.Br(),
                            dcc.Graph(figure=fig4)], width=5, style={"height": "50vh"})
                    , dbc.Col([html.H3("Assignment",style={'margin-left':'15px'}),
                            dbc.Progress(label=assignment_perc, value=assignment_perc, max=100, striped=True,
                                            color="success", style={'hight': '20px','margin-left' :'20px'}), html.Br(),
                            dcc.Graph(figure=fig5)], width=5, style={"height": "50vh"})], justify='left'),
                dbc.Row([dbc.Col([html.H3("URL",style={'margin-left':'15px'}),
                                dbc.Progress(label=url_perc, value=url_perc, max=100, striped=True, color="success",
                                            style={'hight': '20px','margin-left' :'20px'}), html.Br(),
                                dcc.Graph(figure=fig6)], width=5, style={"height": "50vh"})
                            , dbc.Col([html.H3("File",style={'margin-left':'15px'}),
                                    dbc.Progress(label=file_perc, value=file_perc, max=100, striped=True,
                                                    color="success", style={'hight': '20px','margin-left' :'20px'}), html.Br(),
                                    dcc.Graph(figure=fig7)], width=5, style={"height": "50vh"})], justify='left')
                                            ])