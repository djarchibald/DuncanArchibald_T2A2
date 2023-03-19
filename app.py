import os
from dotenv import load_dotenv
load_dotenv()

from datetime import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

db = SQLAlchemy()
ma = Marshmallow()
#CONFIG

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.app_config")
    
    db.init_app(app)
    ma.init_app(app)

    from command.db import db_cmd
    app.register_blueprint(db_cmd)
    
    from controller import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app


