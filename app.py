from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializar la app Flask y cargar configuración
app = Flask(__name__)
app.config.from_object(Config)

# Configurar SQLAlchemy con la app
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)