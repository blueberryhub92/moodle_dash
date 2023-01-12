from functools import wraps
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app, User, server
from flask_login import login_user
from werkzeug.security import check_password_hash
import requests
from flask import redirect, request, jsonify, session, make_response

from group_assessment.assessment import GroupAssessment
from group_overall_progress.overall_progress import GroupOverallProgress
from group_planning.planning import GroupPlanning

#  list of all the enrolled users
eu = ['anonfirstname31 anonlastname31', 'anonfirstname62 anonlastname62', 'anonfirstname65 anonlastname65',
    'anonfirstname51 anonlastname51', 'anonfirstname66 anonlastname66', 'anonfirstname47 anonlastname47',
    'anonfirstname48 anonlastname48', 'anonfirstname68 anonlastname68', 'anonfirstname59 anonlastname59',
    'anonfirstname64 anonlastname64', 'anonfirstname67 anonlastname67', 'anonfirstname53 anonlastname53',
    'anonfirstname49 anonlastname49', 'anonfirstname55 anonlastname55', 'anonfirstname73 anonlastname73',
    'anonfirstname60 anonlastname60', 'anonfirstname57 anonlastname57', 'anonfirstname70 anonlastname70',
    'anonfirstname63 anonlastname63', 'anonfirstname54 anonlastname54', 'anonfirstname56 anonlastname56',
    'anonfirstname61 anonlastname61', 'anonfirstname69 anonlastname69', 'anonfirstname58 anonlastname58',
    'anonfirstname52 anonlastname52', 'anonfirstname71 anonlastname71', 'anonfirstname72 anonlastname72',
    'anonfirstname21 anonlastname21']

enrolled_usernames = [i.replace('firstname', "").replace('lastname', "") for i in eu]
enrolled_usernames = [i.split(" ", 1)[0] for i in enrolled_usernames]

layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlLogin', refresh=True),
        html.Div([
            dbc.Container(
                html.Img(
                    src='/assets/Mobile-M-Icon-1-corners.png',
                    className='center',
                    style={'height':100,'width':100,"padding":"5px"}
                ),
            ),
            dbc.Container(id='loginType', children=[
                dcc.Input(
                    placeholder='Enter your username',
                    type='text',
                    id='usernameBox',
                    className='form-control',
                    n_submit=0,
                ),
                html.Br(),
                dcc.Input(
                    placeholder='Enter your password',
                    type='password',
                    id='passwordBox',
                    className='form-control',
                    n_submit=0,
                ),
                html.Br(),
                html.Button(
                    children='Login',
                    n_clicks=0,
                    type='submit',
                    id='loginButton',
                    className='btn btn-primary btn-lg'
                ),
                html.Br(),
            ], className='form-group'),
        ]),
    ], className='jumbotron')
])



################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - REDIRECT TO PAGE1 IF LOGIN DETAILS ARE CORRECT
################################################################################
@app.callback(Output('urlLogin', 'pathname'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def sucess(n_clicks, usernameSubmit, passwordSubmit, username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if username in enrolled_usernames:
            if user.password == password:
                login_user(user)
                with open("current_user/example.txt", "w") as file:
                    file.write(username)
                # requests.post('http://localhost:8050/process_key', data={'username': username})
                requests.post('http://localhost:8050/process_assessment', data={'username': username})
                requests.post('http://localhost:8050/process_overall_progress', data={'username': username})
                requests.post('http://localhost:8050/process_planning', data={'username': username})
                return '/home'
            else:
                pass
        else:
            pass



################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF LOGIN DETAILS INCORRECT
################################################################################
@app.callback(Output('usernameBox', 'className'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                return 'form-control'
            else:
                return 'form-control is-invalid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF LOGIN DETAILS INCORRECT
################################################################################
@app.callback(Output('passwordBox', 'className'),
              [Input('loginButton', 'n_clicks'),
              Input('usernameBox', 'n_submit'),
              Input('passwordBox', 'n_submit')],
              [State('usernameBox', 'value'),
               State('passwordBox', 'value')])
def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
    if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                return 'form-control'
            else:
                return 'form-control is-invalid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'
