from functools import wraps
from flask import session, redirect, flash

def loguin_requerid(f):
    """Decorador para verificar que el usuario este logueado"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usr_id' not in session:
            flash("Debes iniciar sesion")
            return redirect('/login')
        return f(*args, **kwargs)
    
    return decorated_function
