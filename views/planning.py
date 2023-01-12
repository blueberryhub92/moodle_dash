from flask import session
import dash
import requests
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from app import app, server
from group_planning.planning import GroupPlanning

dash.register_page(__name__,
                   path='/planning',
                   name='Planning',
                   title='Planning')

layout = html.Div([
    html.Div(id='output-div3')
])

@app.server.route('/api/group/planning')
def get_planning():
    instance_of_overall_progress = GroupPlanning(app=server)
    return instance_of_overall_progress.operation()

@app.callback(
    dash.dependencies.Output('output-div3', 'children'),
    [dash.dependencies.Input('url', 'pathname')])
def update_output(pathname):
    if pathname is None:
        return "Wait for the page to load"
    else:
        url = 'http://localhost:8050/api/group/assessment'
        response = requests.get(url)
        data = response.json()


        # This is a dummy list of assignments, that we can iterate over to display on the page
        assignments = [
            {'title': 'Assigment 1', 'desc': 'Blablabla'},
            {'title': 'Assigment 2', 'desc': 'Blablabla'},
            {'title': 'Assigment 3', 'desc': 'Blablabla'},
            {'title': 'Assigment 4', 'desc': 'Blablabla'},
            {'title': 'Assigment 5', 'desc': 'Blablabla'},
            {'title': 'Assigment 6', 'desc': 'Blablabla'},
            {'title': 'Assigment 7', 'desc': 'Blablabla'}
        ]
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
            html.H1(
                'Planning page',
                style={'margin-bottom': '2rem'}
            ),
            html.H2('This is a list of items, to show you how to iterate and use bootstrap components'),
            html.Ul(
                [
                    html.Li(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4(assignment['title'], className='card-title'),
                                    html.P(assignment['desc'], className='card-text')
                                ]
                            )
                        ),
                        style={'margin-bottom': '1rem', 'background-color':'grey'}
                    ) for assignment in assignments
                ],
                style={'list-style': 'none', 'padding': '0', 'margin-bottom': '5rem', 'color':'grey'}
            ),
            html.H2('Simple chart from a python dict'),
            dcc.Graph(
                figure=dict_figure,
                style={'margin-bottom': '5rem'}
            ),
            html.H2('Simple chart from a plotly graph object'),
            dcc.Graph(figure=graph_object_figure)
        ])


