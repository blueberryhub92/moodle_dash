# Dash app initialization
import dash
# User management initialization
import os
from flask_login import LoginManager, UserMixin
from users_mgt import db, mdl_user as base
from config import URI
from flask import Flask
from flask_session import Session
from flask_cors import CORS

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

