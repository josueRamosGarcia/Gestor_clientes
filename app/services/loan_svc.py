from ..repositories.loan_repo import LoanRepository
from ..utils.helpers import filter_data
from flask import current_app

class LoanService:
    def __init__(self):
        self.loan_repo = LoanRepository()

    def __getattr__(self, name):
        return getattr(self.loan_repo, name)
    
    def process_loans(self, form, cl_id):
        i = 0

        while f'prestamos[{i}][prst_financiera]' in form:
            cat = form.get(f'prestamos[{i}][prst_cat]') #ln_cat[{i}]
            amount = form.get(f'prestamos[{i}][prst_monto]')
            discount = form.get(f'prestamos[{i}][prst_descuento]')
            term = form.get(f'prestamos[{i}][prst_plazo]')
            amount_pay = form.get(f'prestamos[{i}][prst_imp_pagar]')
            f_disc_dt = form.get(f'prestamos[{i}][prst_f_p_desc]')
            fi_id = form.get(f'prestamos[{i}][prst_financiera]')
            lt_id = form.get(f'prestamos[{i}][tp_id]')
            ls_id = form.get(f'prestamos[{i}][ep_id]')

            data = filter_data({
                'ln_cat': cat,
                'ln_amount': amount,
                'ln_discount':discount,
                'ln_term': term,
                'ln_am_pay': amount_pay,
                'ln_f_disc_dt': f_disc_dt,
                'cl_id': cl_id,
                'fi_id': fi_id,
                'lt_id': lt_id,
                'ls_id': ls_id
            })

            try:
                self.create(**data)
            except Exception as e:
                current_app.logger.warning(f"Error creando prestamo {i}: {e}")

            i += 1