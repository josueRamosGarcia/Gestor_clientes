from .base_repository import BaseRepository
from ..models.cliente import Cliente

class ClienteRepository(BaseRepository):
    def __init__(self):
        super().__init__(Cliente)
        self.id_field = "cte_id"

    def search_by_name(self, busqueda):
        return self.db.session.query(self.model).filter(
            self.db.or_(
                Cliente.cte_nombre.ilike(f"%{busqueda}%"),
                Cliente.cte_apellidos.ilike(f"%{busqueda}%")
            )
        ).all()
