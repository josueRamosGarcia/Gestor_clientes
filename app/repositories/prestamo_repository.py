from .base_repository import BaseRepository
from ..models.prestamo import Prestamo, TipoPrestamo, EstatusPrestamo

class PrestamoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Prestamo)
        self.id_field = "prst_id"

    def get_by_cte_id(self, cte_id):
        return self.db.session.query(self.model).filter_by(
            cte_id = cte_id
        ).all()

    def get_status(self):
        return self.db.session.query(EstatusPrestamo).all()
    
    def get_tipos(self):
        return self.db.session.query(TipoPrestamo).all()