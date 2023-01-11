# index page
import json
import requests
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app, server
from flask_login import logout_user, current_user
from views import login, error, overall_progress, assessment, planning, home, profile
from flask import session

navBar = dbc.Navbar(id='navBar',
    children=[],
    sticky='top',
    color='primary',
    className='navbar navbar-expand-lg navbar-dark bg-primary',
    style={'background': 'linear-gradient(0deg, #e15707 0, #f28224 100%)'}
)

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    'margin-top': 10,
    "height": "100%",
    'border-radius': 20,
    # "transition": "margin-left .5s",
    "margin-left": "1rem",
    "margin-right": "1rem",
    "padding": "2rem 1rem",
    'background': 'linear-gradient(0deg, #e15707 0, #f28224 100%)',
    'color': 'white'
}

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        navBar,
        html.Div(id='pageContent',style=CONTENT_STYLE),
        
    ])
], id='table-wrapper')


################################################################################
# HANDLE PAGE ROUTING - IF USER NOT LOGGED IN, ALWAYS RETURN TO LOGIN SCREEN
################################################################################
@app.callback(Output('pageContent', 'children'),
              [Input('url', 'pathname')])
def displayPage(pathname):
    if pathname == '/' or pathname == '/home':
        if current_user.is_authenticated:
            return home.layout
        else:
            return login.layout 

    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return login.layout
        else:
            return login.layout

    if pathname == '/overall_progress':
        if current_user.is_authenticated:
            # response = requests.get('http://127.0.0.1:8050/api/group/overall_progress')
            # data = response.json()
            # return html.Div([
            #     html.H1(f'Data from Flask: {data}'),
            #     overall_progress.layout
            # ])
            response = server.test_client().get('/api/group/overall_progress')
            json_data = json.loads(response.data.decode())
            with open('data.txt', 'w') as file:
                file.write(json.dumps(json_data))
            return overall_progress.layout
        else:
            return login.layout

    if pathname == '/assessment':
        if current_user.is_authenticated:
            return assessment.layout
        else:
            return login.layout
    
    if pathname == '/planning':
        if current_user.is_authenticated:
            return planning.layout
        else:
            return login.layout

    if pathname == '/profile':
        if current_user.is_authenticated:
            return profile.layout
        else:
            return login.layout

    if pathname == '/admin':
        if current_user.is_authenticated:
            if current_user.admin == 1:
                return user_admin.layout
            else:
                return error.layout
        else:
            return login.layout


    else:
        return error.layout


################################################################################
# ONLY SHOW NAVIGATION BAR WHEN A USER IS LOGGED IN
################################################################################
@app.callback(
    Output('navBar', 'children'),
    [Input('pageContent', 'children')])
def navBar(input1):
    if current_user.is_authenticated:
        navBarContents = [
            dbc.NavItem(dbc.NavLink('Home', href='/home')),
            dbc.NavItem(dbc.NavLink('Overall Progress', href='/overall_progress')),
            dbc.NavItem(dbc.NavLink('Assessment', href='/assessment')),
            dbc.NavItem(dbc.NavLink('Planning', href='/planning')),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label=current_user.username,
                children=[
                    dbc.DropdownMenuItem('Profile', href='/profile'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem('Logout', href='/logout'),
                ],
            ),
            html.Img(src='/assets/Mobile-M-Icon-1-corners.png', className="ml-auto", style={'height':'4%', 'width':'4%'}),
        ]
        return navBarContents

    else:
        return ''



if __name__ == '__main__':
    app.run_server(debug=True)
