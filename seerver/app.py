from flask import Flask
from config import Config
from flask_bcrypt import Bcrypt
# from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS 

import os

app = Flask(__name__)
app.config.from_object(Config)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)
# ma = Marshmallow(app)

from src.services.database import session, init_db, teardown_session
from src.models import User, Attendance
init_db(app)

from src.routes import camera_routes, user_routes

@app.route('/')
def main_page():
    return 'Main page'

# Run application
if __name__ == '__main__':
    app.run()
