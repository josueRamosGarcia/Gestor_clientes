from flask import Blueprint, render_template, request, session, redirect
from ..services.auth_service import AuthService
from ..utils.helpers import get_client_ip

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def inicio():
    return render_template('login.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    auth_service = AuthService()

    username = request.form.get('usuario')
    password = request.form.get('contraseña')

    user, error = auth_service.authenticate_user(username, password)

    if error:
        return redirect('/login')
    
    session['usr_id'] = user.usr_id
    session['ses_ip'] = get_client_ip()

    return render_template('inicio.html')
