from ..repositories.prestamo_repository import PrestamoRepository
from ..utils.helpers import filtrar_datos
from flask import current_app

class PrestamoService:
    def __init__(self):
        self.prst_repo = PrestamoRepository()

    def __getattr__(self, name):
        return getattr(self.prst_repo, name)
    
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