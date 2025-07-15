from flask import Flask
from config.database import db
from config.settings import Config
from .controllers.auth_controller import auth_bp
from .controllers.client_controller import cte_bp
import secrets

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = secrets.token_hex(16)

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(cte_bp)

    return app