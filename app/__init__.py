from flask import Flask
from config.database import db
from config.settings import Config
from .controllers.user_ctrl import user_bp
from .controllers.client_ctrl import client_bp
import secrets

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = secrets.token_hex(16)

    db.init_app(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(client_bp)

    return app