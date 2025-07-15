from flask import Blueprint, render_template, request, session, redirect
from ..services.auth_service import AuthService
from ..utils.helpers import get_client_ip

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def inicio():
    return render_template('login.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('usuario')
    password = request.form.get('contraseña')

    auth_service = AuthService()
    user, error = auth_service.authenticate_user(username, password)

    if error:
        return redirect('/login')
    
    session['usr_id'] = user.usr_id
    session['ses_ip'] = get_client_ip()

    return render_template('inicio.html', nombre_usuario=user.usr_username)
