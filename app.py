# Dash app initialization
import dash
# User management initialization
import os
from flask_login import LoginManager, UserMixin, login_required
from users_mgt import db, mdl_user as base
from config import URI
from flask import Flask, jsonify,redirect, render_template, session, request
import dash_bootstrap_components as dbc
import json
from flask_session import Session
from flask_cors import CORS
from flask_login import login_required, current_user
import requests
from group_assessment.assessment import GroupAssessment
from group_overall_progress.overall_progress import GroupOverallProgress
from group_planning.planning import GroupPlanning

server = Flask(__name__)
server.config["SECRET_KEY"] = "topSecret"
app = dash.Dash(__name__, server=server)

app.config.suppress_callback_exceptions = True
CORS(server, origins=['*'])

# config
server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI=URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    TEMPLATES_AUTO_RELOAD = True
)

# Configure the session to use filesystem storage
server.config['SESSION_TYPE'] = 'filesystem'
Session(server)

db.init_app(server)

server.app_context().push()


# Setup the LoginManager for the server
login_manager = LoginManager(server)
login_manager.init_app(server)
login_manager.login_view = '/login'


# Create User class with UserMixin
class User(UserMixin, base):
    pass

# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.server.route('/process_assessment', methods=['POST'])
def post_assessment():
    user = request.form['username']
    session['user'] = user
    return redirect('/api/group/assessment')

@app.server.route('/process_overall_progress', methods=['POST'])
def post_overall_progress():
    user = request.form['username']
    session['user'] = user
    return redirect('/api/group/overall_progress')

@app.server.route('/process_planning', methods=['POST'])
def post_planning():
    user = request.form['username']
    session['user'] = user
    return redirect('/api/group/planning')

@app.server.route('/api/group/assessment')
def get_assessment():
    user = session.get('user')
    instance_of_assessment = GroupAssessment(app=server, user=user)
    return instance_of_assessment.operation()

@app.server.route('/api/group/overall_progress')
def get_overall_progress():
    user = session.get('user')
    instance_of_overall_progress = GroupOverallProgress(app=server, user=user)
    return instance_of_overall_progress.operation()

@app.server.route('/api/group/planning')
def get_planning():
    user = session.get('user')
    instance_of_overall_progress = GroupPlanning(app=server, user=user)
    return instance_of_overall_progress.operation()

