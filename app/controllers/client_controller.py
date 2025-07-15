from flask import Blueprint, request, render_template
from ..services.auth_service import AuthService
from ..services.cliente_service import ClienteService
from ..utils.decorators import loguin_requerid

cte_bp = Blueprint('cte_bp', __name__)

@cte_bp.route('/buscar_clientes', methods=['POST'])
@loguin_requerid
def buscar_clientes():
    auth_service = AuthService()
    cte_service = ClienteService()

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
