from ..repositories.cliente_repository import ClienteRepository
from ..repositories.prestamo_repository import PrestamoRepository
from .archivos_service import ArchivoServices
from ..utils.helpers import filtrar_datos
from flask import current_app


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
