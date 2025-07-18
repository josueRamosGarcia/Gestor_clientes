from flask import Blueprint, request, render_template, redirect
from ..services.auth_service import AuthService
from ..services.cliente_service import ClienteService
from ..utils.decorators import loguin_requerid

cte_bp = Blueprint('cte_bp', __name__)

auth_service = AuthService()
cte_service = ClienteService()

@cte_bp.route('/buscar_clientes', methods=['POST'])
@loguin_requerid
def buscar_clientes():

    busqueda = request.form.get('busqueda','').strip()
    user = auth_service.get_logged_user()   

    if busqueda:
        clientes = cte_service.search_by_name(busqueda)

        return render_template(
            'inicio.html',
            nombre_usuario=user.usr_username,
            clientes=clientes,
            busqueda=busqueda
        )

@cte_bp.route('/cliente/<int:cte_id>')
@loguin_requerid
def detalle_cliente(cte_id):
    cliente, prestamos = cte_service.get_client_and_credits(cte_id)

    return render_template(
        'details_clientes.html',
        cliente=cliente,
        prestamos=prestamos
    )

@cte_bp.route('/agregar_cliente')
@loguin_requerid
def agregar_cliente():
    estatus_clientes = cte_service.get_status()

    return render_template(
        'add_clientes.html',
        estatus_clientes=estatus_clientes
    )

@cte_bp.route('/subir_cliente', methods=['POST'])
@loguin_requerid
def subir_cliente():
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')
    curp = request.form.get('curp')
    nss = request.form.get('nss')
    rfc = request.form.get('rfc')
    id_estatus = request.form.get('estatus')

    datos_cliente = {
        'cte_nombre': nombre,
        'cte_apellidos' : apellidos,
        'cte_curp': curp,
        'cte_nss' : nss,
        'cte_rfc' : rfc,
        'ec_id': id_estatus
    }

    datos_filtrados = {k: v for k, v in datos_cliente.items() if v}

    cte_service.create_client(**datos_filtrados)

    id = cte_service.get_client_id(curp)[0]
    
    return redirect(f'/cliente/{id}')