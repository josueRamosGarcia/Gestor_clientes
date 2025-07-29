from flask import (
    Blueprint, request, render_template, redirect,
    url_for, current_app, flash   
)
from ..services.user_svc import UserService
from ..services.client_svc import ClientService
from ..services.file_svc import FileService
from ..services.loan_svc import LoanService
from ..utils.decorators import loguin_requerid
from cloudinary.utils import cloudinary_url

client_bp = Blueprint('client_bp', __name__)

user_svc = UserService()
client_svc = ClientService()
file_svc = FileService()
loan_svc = LoanService()

@client_bp.route('/search_client', methods=['POST'])
@loguin_requerid
def search_client():
    search = request.form.get('search','').strip()
    user = user_svc.get_logged_user()   

    if search:
        clients = client_svc.search_by_name(search)

        return render_template(
            'inicio.html',
            username = user.usr_username,
            clients = clients,
            search = search
        )

@client_bp.route('/cliente/<int:cte_id>')
@loguin_requerid
def detalle_cliente(cte_id):
    client, prestamos = client_svc.get_client_and_credits(cte_id)

    return render_template(
        'details_clientes.html',
        client = client,
        prestamos = prestamos,
        client_status = client_svc.get_status()
    )

@client_bp.route('/agregar_cliente')
@loguin_requerid
def agregar_cliente():
    return render_template(
        'add_clientes.html',
        estatus_clientes = client_svc.get_status(),
        tipos_archivos = file_svc.get_file_types(),
        tipos_prestamos = loan_svc.get_types(),
        financieras = loan_svc.get_financial_institutions(),
        estatus_prestamos = loan_svc.get_status()
    )

@client_bp.route('/subir_cliente', methods=['POST'])
@loguin_requerid
def subir_cliente():
    try:
        form = request.form
        files = request.files

        em_id = client_svc.process_email(form)
        cl_id = client_svc.process_client(form, em_id)

        file_svc.process_files(files, form, cl_id)
        client_svc.process_phone_numbers(form, cl_id)
        loan_svc.process_loans(form, cl_id)
    
        return redirect(url_for('client_bp.detalle_cliente', cte_id = cl_id))
    
    except Exception as e:
        current_app.logger.exception("Error al subir cliente")
        flash("Ocurrió un error al subir los datos del cliente.")
        return redirect(request.referrer)