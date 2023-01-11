import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app
from flask_login import current_user

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlProfile', refresh=True),
        html.H3('Profile Management', style={'color':'grey'}),
        html.Hr(),
        dbc.Row([

            dbc.Col([
                dbc.Label('Username:', style={'color':'grey'}),
                html.Br(),
                html.Br(),
                dbc.Label('Email:', style={'color':'grey'}),
            ], md=2),

            dbc.Col([
                dbc.Label(id='username', className='text-success'),
                html.Br(),
                html.Br(),
                dbc.Label(id='email', className='text-success'),
            ], md=4),
        ]),
    ], className='jumbotron')
])


@app.callback(
    Output('username', 'children'),
    [Input('pageContent', 'children')])
def currentUserName(pageContent):
    try:
        username = current_user.username
        return username
    except AttributeError:
        return ''


@app.callback(
    Output('email', 'children'),
    [Input('pageContent', 'children')])
def currentUserEmail(pageContent):
    try:
        email = current_user.email
        return email
    except AttributeError:
        return ''
