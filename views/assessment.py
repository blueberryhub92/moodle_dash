from flask import session
import dash
import requests
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from app import app, server
from group_assessment.assessment import GroupAssessment

dash.register_page(__name__,
                   path='/assessment',
                   name='Assessment',
                   title='Assessment')

layout = html.Div([
    html.Div(id='output-div2')
])

@app.server.route('/api/group/assessment')
def get_assessment():
    instance_of_assessment = GroupAssessment(app=server)
    return instance_of_assessment.operation()

@app.callback(
    dash.dependencies.Output('output-div2', 'children'),
    [dash.dependencies.Input('url', 'pathname')])
def update_output(pathname):
    if pathname is None:
        return "Wait for the page to load"
    else:
        url = 'http://localhost:8050/api/group/assessment'
        response = requests.get(url)
        data = response.json()

        # This is a python dict, that can be used to create a bar chart
        dict_figure = {
            'data': [
                {
                    'x': ['Assignment 1', 'Assignment 2', 'Assignment 3'],
                    'y': [10, 1, 5],
                    'type': 'bar',
                    'name': 'Grades'
                }
            ],
            'layout': {
                'title': 'Assignment grades'
            }
        }
        # This is a plotly graph object to create the same bar chart
        graph_object_figure = go.Figure(
            data=[go.Bar(x=['Assignment 1', 'Assignment 2', 'Assignment 3'], y=[10, 1, 5])],
            layout=go.Layout(
                title=go.layout.Title(text='Assignment grades')
            )
        )


        # This is the html layout, that is displayed on the page
        return html.Div(children=[
            html.H1('Assessment page', style={'margin-bottom': '2rem'}),
            html.H2('Just a simple button, to show you how to use bootstrap components'),
            dbc.Button(
                "Click me, but I won't do anything!",
                color="primary",
                style={'margin-bottom': '5rem'}
            ),
            html.H2('Simple chart from a python dict'),
            dcc.Graph(
                figure=dict_figure,
                style={'margin-bottom': '5rem'}
            ),
            html.H2('Simple chart from a plotly graph object'),
            dcc.Graph(figure=graph_object_figure)
        ])


