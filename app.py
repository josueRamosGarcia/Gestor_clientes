from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from config import Config
from models import db, Usuario
import secrets



# Inicializar la app Flask y cargar configuración
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = secrets.token_hex(16)

# Configurar SQLAlchemy con la app
db = SQLAlchemy(app)

# RUTAS
@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    nombre_usuario = request.form['usuario']
    contraseña = request.form['contraseña']

    usuario = db.session.query(Usuario).filter_by(
        usr_username=nombre_usuario
    ).first()

    usuario_val = usuario is not None
    contraseña_val = usuario_val and check_password_hash(usuario.usr_pass, contraseña)
    activo = usuario_val and usuario.usr_activo

    if not (usuario_val and contraseña_val and activo):
        flash("Usuario o contraseña incorrectos")
        return redirect('/login')

    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)