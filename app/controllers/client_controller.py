from flask import Blueprint, request, render_template, redirect, url_for, current_app, flash
from ..services.auth_service import AuthService
from ..services.cliente_service import ClienteService
from ..services.archivos_service import ArchivoServices
from ..utils.decorators import loguin_requerid
from ..utils.helpers import filtrar_datos

from cloudinary.utils import cloudinary_url

cte_bp = Blueprint('cte_bp', __name__)

auth_service = AuthService()
cte_service = ClienteService()
arch_service = ArchivoServices()

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
    estatus = cte_service.get_status()

    return render_template(
        'details_clientes.html',
        cliente=cliente,
        prestamos=prestamos,
        estatus_clientes=estatus
    )

@cte_bp.route('/agregar_cliente')
@loguin_requerid
def agregar_cliente():
    estatus_clientes = cte_service.get_status()
    tiposarchivos = arch_service.get_file_types()

    return render_template(
        'add_clientes.html',
        estatus_clientes=estatus_clientes,
        tipos_archivos = tiposarchivos
    )

@cte_bp.route('/subir_cliente', methods=['POST'])
@loguin_requerid
def subir_cliente():
    try:
        form = request.form
        files = request.files

        id_correo = cte_service.procesar_correo(form)
        id_cliente = cte_service.procesar_cliente(form, id_correo)

        cte_service.procesar_archivos(files, form, id_cliente)
        cte_service.procesar_telefonos(form, id_cliente)
        cte_service.procesar_prestamos(form, id_cliente)
    
        return redirect(url_for('cte_bp.detalle_cliente', cte_id=id_cliente))
    
    except Exception as e:
        current_app.logger.exception("Error al subir cliente")
        flash("Ocurrió un error al subir los datos del cliente.")
        return redirect(request.referrer)