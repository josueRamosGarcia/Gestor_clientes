from flask import Blueprint, render_template, request, session, redirect
from ..services.auth_service import AuthService
from ..utils.helpers import get_client_ip
from ..utils.decorators import loguin_requerid

auth_bp = Blueprint('auth', __name__)

auth_service = AuthService()

@auth_bp.route('/')
def login_page():
    return render_template('login.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('usuario')
    password = request.form.get('contraseña')

    user, error = auth_service.authenticate_user(username, password)

    if error:
        return redirect('/login')
    
    session['usr_id'] = user.usr_id
    session['ses_ip'] = get_client_ip()

    return render_template('inicio.html', nombre_usuario=user.usr_username)

@auth_bp.route('/inicio')
@loguin_requerid
def inicio():
    usr = auth_service.get_logged_user()

    return render_template('/inicio.html', nombre_usuario=usr.usr_username)