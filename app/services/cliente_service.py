from ..repositories.cliente_repository import ClienteRepository
from ..repositories.prestamo_repository import PrestamoRepository

class ClienteService:
    def __init__(self):
        self.cte_repo = ClienteRepository()
        self.prst_repo = PrestamoRepository()

    def get_client_and_credits(self, id):
        cliente = self.cte_repo.get_by_id(id)
        prestamos = self.prst_repo.get_by_cte_id(id)

        return cliente, prestamos
        
    def search_by_name(self, busqueda):
        return self.cte_repo.search_by_name(busqueda)
    
    def create_client(self, **kwargs):
        return self.cte_repo.create(**kwargs)
    
    def get_status(self):
        return self.cte_repo.get_estatus()

    def get_client_id(self, curp):
        return self.cte_repo.get_client_id(curp)