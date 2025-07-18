from .base_repository import BaseRepository
from ..models.cliente import Cliente, EstatusCliente, Correo

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

    def get_estatus(self):
        return self.db.session.query(EstatusCliente).all()
    
    def get_client_id(self, curp):
        return self.db.session.query(Cliente.cte_id).filter_by(
            cte_curp = curp
        ).first()
    
    def create_correo(self,**kwargs):
        instance = Correo(**kwargs)
        self.db.session.add(instance)
        self.db.session.commit()
        return instance
    
    def get_corr_id(self, nombre):
        return self.db.session.query(Correo.corr_id).filter_by(
            corr_nombre = nombre
        ).first()