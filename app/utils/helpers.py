from flask import request, session

def get_client_ip():
    """"Funcion para obtener la ip real del cliente"""
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    elif request.headers.get('X-Real-IP'):
        ip = request.headers.get('X-Real-IP')
    else:
        ip = request.remote_addr
    return ip

def get_usr_id_log():
    """Obtener el usuario logueado de la sesión"""
    return session.get('usr_id')

def filter_data(dicc):
    return {k: v for k, v in dicc.items() if v}