from ..repositories.client_repo import ClientRepository
from ..repositories.loan_repo import LoanRepository
from ..utils.helpers import filter_data
from flask import current_app

class ClientService:
    def __init__(self):
        self.client_repo = ClientRepository()
        self.loan_repo = LoanRepository()

    def __getattr__(self, name):
        return getattr(self.client_repo, name)
    
    def get_client_and_credits(self, id):
        client = self.client_repo.get_by_id(id)
        loans = self.loan_repo.get_by_cl_id(id)

        return client, loans
    
    def process_client(self, form, em_id):
        name = form.get('nombre')
        lname = form.get('apellidos')
        curp = form.get('curp')
        nss = form.get('nss')
        rfc = form.get('rfc')
        cs_id = form.get('estatus')

        data = filter_data({
            'cl_name': name,
            'cl_lname' : lname,
            'cl_curp': curp,
            'cl_nss' : nss,
            'cl_rfc' : rfc,
            'cs_id': cs_id,
            'em_id' : em_id
        })

        self.create(**data)
        return self.get_client_id_by_curp(curp)[0]

    def process_email(self, form):
        email = form.get('corr_nombre')

        if email:
            password = form.get('corr_contraseña')
            location = form.get('corr_localizacion')

            data = filter_data({
                'em_name' : email,
                'em_password' : password,
                'em_location' : location
            })

            self.create_email(**data)
            return self.get_email_id_by_name(email)[0]
        else:
            return None
        
    
    def process_phone_numbers(self, form, cl_id):
        i = 0

        while f'telefonos[{i}][tel_telefono]' in form:
            phone_numer = form.get(f'telefonos[{i}][tel_telefono]')
            name =  form.get(f'telefonos[{i}][tel_nombre]')
            relation = form.get(f'telefonos[{i}][tel_parentesco]')

            data = filter_data({
                'ph_numeber': phone_numer,
                'ph_name':name,
                'ph_rel': relation,
                'cl_id': cl_id
            })

            try:
                self.create_phone_number(**data)
            except Exception as e:
                current_app.logger.warning(f"Error creando teléfono {i}: {e}")

            i += 1
