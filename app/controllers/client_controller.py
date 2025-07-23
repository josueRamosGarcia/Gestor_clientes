from flask import Blueprint, request, render_template, redirect
from ..services.auth_service import AuthService
from ..services.cliente_service import ClienteService
from ..services.archivos_service import ArchivoServices
from ..utils.decorators import loguin_requerid
from ..utils.helpers import filtrar_datos
import cloudinary
import cloudinary.uploader
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
    # Insertar datos correo
    correo = request.form.get('corr_nombre')

    if correo:
        contraseña = request.form.get('corr_contraseña')
        localizacion = request.form.get('corr_localizacion')

        datos_correo = {
            'corr_nombre' : correo,
            'corr_contraseña' : contraseña,
            'corr_localizacion' : localizacion
        }

        corr_datos_fil = filtrar_datos(datos_correo)
        cte_service.create_correo(**corr_datos_fil)
        id_correo = cte_service.get_corr_id(correo)[0]
    else:
        id_correo = None

    # Insertar datos cliente
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
        'ec_id': id_estatus,
        'corr_id' : id_correo
    }

    cte_datos_fil = filtrar_datos(datos_cliente)
    cte_service.create_client(**cte_datos_fil)

    id = cte_service.get_client_id(curp)[0]


    # Subir archivos
    if 'archivos' in request.files:
        files = request.files.getlist('archivos')
        print(f"Número de archivos: {len(files)}")
        
        for index, file in enumerate(files):
            if file.filename != '':
                # Obtener metadatos del archivo usando el índice
                ta_id_key = f'archivos_info[{index}][ta_id]'
                arch_nombre_key = f'archivos_info[{index}][arch_nombre]'
                
                ta_id = request.form.get(ta_id_key)
                arch_nombre = request.form.get(arch_nombre_key)
                
                if ta_id and arch_nombre:
                    try:
                        upload_result = cloudinary.uploader.upload(
                            file,
                            folder=f"clientes/{id}/",
                            public_id=arch_nombre,
                            use_filename=True,
                            unique_filename=False,
                            resource_type="auto",
                        )

                        # Optimize delivery by resizing and applying auto-format and auto-quality
                        optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")

                        datos_archivo = {
                            'arch_url': optimize_url,
                            'arch_nombre':arch_nombre,
                            'ta_id': ta_id,
                            'cte_id': id
                        }

                        arch_datos_fil = filtrar_datos(datos_archivo)
                        arch_service.create_archivo(**arch_datos_fil)
                        
                    except Exception as upload_error:
                        print(f"Error subiendo archivo {index}: {str(upload_error)}")
                        import traceback
                        traceback.print_exc()
                else:
                    print(f"Faltan metadatos para archivo {index}")
            else:
                print(f"Archivo {index} está vacío")

    return redirect(f'/cliente/{id}')