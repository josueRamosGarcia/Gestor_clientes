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

        while f'prestamos[{i}][fi_id]' in form:
            cat = form.get(f'ln_cat[${i}]')
            amount = form.get(f'ln_monto[${i}]')
            discount = form.get(f'ln_descuento[${i}]')
            term = form.get(f'ln_plazo[${i}]')
            amount_pay = form.get(f'ln_imp_pagar[${i}]')
            f_disc_dt = form.get(f'ln_f_p_desc[${i}]')
            fi_id = form.get(f'ln_fi_id[${i}]')
            lt_id = form.get(f'ln_tp_id[${i}]')
            ls_id = form.get(f'ln_ep_id[${i}]')

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