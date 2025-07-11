from flask import Flask, request, redirect, render_template, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from config import Config
from models import db, Usuario, Cliente
import secrets

# Inicializar la app Flask y cargar configuración
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = secrets.token_hex(16)

# Configurar SQLAlchemy con la app
db = SQLAlchemy(app)

def get_client_ip():
    """Función para obtener la IP real del cliente"""
    # Verificar si viene de un proxy o load balancer
    if request.headers.get('X-Forwarded-For'):
        # Tomar la primera IP de la lista (IP real del cliente)
        ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    elif request.headers.get('X-Real-IP'):
        ip = request.headers.get('X-Real-IP')
    else:
        # IP directa
        ip = request.remote_addr
    
    return ip

def login_required(f):
    """Decorador para verificar que el usuario esté logueado"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usr_id' not in session:
            flash("Debes iniciar sesión para acceder a esta página")
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

def get_usuario_logueado():
    """Obtener el usuario logueado de la sesión"""
    if 'usr_id' in session:
        return db.session.query(Usuario).filter_by(usr_id=session['usr_id']).first()
    return None

# RUTAS
@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
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
    
    session['usr_id'] = usuario.usr_id
    session['ses_ip'] = get_client_ip()

    return render_template('inicio.html', nombre_usuario=usuario.usr_username)

@app.route('/buscar_clientes', methods=['POST'])
@login_required
def buscar_clientes():
    busqueda = request.form.get('busqueda','').strip()
    usuario = get_usuario_logueado()

    if busqueda:
        clientes = db.session.query(Cliente).filter(
            db.or_(
                Cliente.cte_nombre.ilike(f'%{busqueda}%'),
                Cliente.cte_apellidos.ilike(f'%{busqueda}%'),
            )
        ).all()

        return render_template('inicio.html',
                                nombre_usuario=usuario.usr_username, 
                                clientes=clientes, 
                                busqueda=busqueda
                                )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)