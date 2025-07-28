from flask import Blueprint, render_template, request, session, redirect
from ..services.user_svc import UserService
from ..utils.helpers import get_client_ip
from ..utils.decorators import loguin_requerid

user_bp = Blueprint('user', __name__)

user_svc = UserService()

@user_bp.route('/')
def login_page():
    return render_template('login.html')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        session.clear()
        return render_template('login.html')

    username = request.form.get('usuario')
    password = request.form.get('contraseña')

    user, error = user_svc.authenticate_user(username, password)

    if error:
        return redirect('/login')
    
    session['usr_id'] = user.usr_id
    session['ses_ip'] = get_client_ip()

    return redirect('/inicio')

@user_bp.route('/inicio')
@loguin_requerid
def inicio():
    usr = user_svc.get_logged_user()

    return render_template('/inicio.html', nombre_usuario=usr.usr_username)