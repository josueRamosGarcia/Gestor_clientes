from ..repositories.cliente_repository import ClienteRepository
from ..repositories.prestamo_repository import PrestamoRepository
from .archivos_service import ArchivoServices
from ..utils.helpers import filtrar_datos
from flask import current_app
from werkzeug.utils import secure_filename
import cloudinary
import cloudinary.uploader


class ClienteService:
    def __init__(self):
        self.cte_repo = ClienteRepository()
        self.prst_repo = PrestamoRepository()
        self.arch_service = ArchivoServices()

    def get_client_and_credits(self, id):
        cliente = self.cte_repo.get_by_id(id)
        prestamos = self.prst_repo.get_by_cte_id(id)

        return cliente, prestamos
    
    def __getattr__(self, name):
        return getattr(self.cte_repo, name)

    def procesar_correo(self, form):
        correo = form.get('corr_nombre')

        if correo:
            contraseña = form.get('corr_contraseña')
            localizacion = form.get('corr_localizacion')

            datos = filtrar_datos({
                'corr_nombre' : correo,
                'corr_contraseña' : contraseña,
                'corr_localizacion' : localizacion
            })

            self.create_correo(**datos)
            return self.get_corr_id(correo)[0]
        else:
            return None
        
    def procesar_cliente(self, form, id_correo):
        nombre = form.get('nombre')
        apellidos = form.get('apellidos')
        curp = form.get('curp')
        nss = form.get('nss')
        rfc = form.get('rfc')
        id_estatus = form.get('estatus')

        datos = filtrar_datos({
            'cte_nombre': nombre,
            'cte_apellidos' : apellidos,
            'cte_curp': curp,
            'cte_nss' : nss,
            'cte_rfc' : rfc,
            'ec_id': id_estatus,
            'corr_id' : id_correo
        })

        self.create(**datos)
        return self.get_client_id(curp)[0]
    
    def procesar_archivos(self, files, form, cte_id):
        if 'archivos' not in files:
            return
        
        for i, file in enumerate(files.getlist('archivos')):
            if not file or file.filename == '':
                continue

            ta_id = form.get(f'archivos_info[{i}][ta_id]')
            arch_nombre = form.get(f'archivos_info[{i}][arch_nombre]')

            if not ta_id or not arch_nombre:
                current_app.logger.warning(f"Faltan metadatos en archivo[{i}]")

            try:
                safe_name = secure_filename(arch_nombre)
                upload_result = cloudinary.uploader.upload(
                    file,
                    folder=f"clientes/{cte_id}/",
                    public_id=safe_name,
                    use_filename=True,
                    unique_filename=False,
                    resource_type="auto",
                )

                datos = filtrar_datos({
                    'arch_url': upload_result['secure_url'],
                    'arch_nombre': safe_name,
                    'ta_id': ta_id,
                    'cte_id': cte_id
                })

                self.arch_service.create_archivo(**datos)
            except Exception as e:
                current_app.logger.exception(f"Error subiendo archivo {i}")

    def procesar_telefonos(self, form, cte_id):
        i = 0

        while f'telefonos[{i}][tel_telefono]' in form:
            telefono = form.get(f'telefonos[{i}][tel_telefono]')
            nombre =  form.get(f'telefonos[{i}][tel_nombre]')
            parentesco = form.get(f'telefonos[{i}][tel_parentesco]')

            datos = filtrar_datos({
                'tel_telefono': telefono,
                'tel_nombre':nombre,
                'tel_parentesco': parentesco,
                'cte_id': cte_id
            })

            try:
                self.create_telefono(**datos)
            except Exception as e:
                current_app.logger.warning(f"Error creando teléfono {i}: {e}")

            i += 1

    def procesar_prestamos(self, form, cte_id):
        i = 0

        while f'prestamos[{i}][prst_financiera]' in form:
            financiera = form.get(f'prestamos[{i}][prst_financiera]')
            tipo = form.get(f'prestamos[{i}][tp_id]')
            cat = form.get(f'prestamos[{i}][prst_cat]')
            monto = form.get(f'prestamos[{i}][prst_monto]')
            descuento = form.get(f'prestamos[{i}][prst_descuento]')
            plazo = form.get(f'prestamos[{i}][prst_plazo]')
            imp_pagar = form.get(f'prestamos[{i}][prst_imp_pagar]')
            f_p_descuento = form.get(f'prestamos[{i}][prst_f_p_desc]')
            ep = form.get(f'prestamos[{i}][ep_id]')

            datos = filtrar_datos({
                'prst_financiera': financiera,
                'tp_id': tipo,
                'prst_cat': cat,
                'prst_monto': monto,
                'prst_descuento':descuento,
                'prst_plazo': plazo,
                'prst_imp_pagar': imp_pagar,
                'prst_f_p_desc': f_p_descuento,
                'ep_id': ep,
                'cte_id': cte_id
            })

            try:
                self.prst_repo.create(**datos)
            except Exception as e:
                current_app.logger.warning(f"Error creando prestamo {i}: {e}")

            i += 1