from ..repositories.cliente_repository import ClienteRepository
from ..repositories.prestamo_repository import PrestamoRepository

class ClienteService:
    def __init__(
        self,
        cte_repo: ClienteRepository,
        prst_repo: PrestamoRepository
    ):
        self.cte_repo = cte_repo
        self.prst_repo = prst_repo

    def get_client_and_credits(self, id):
        cliente = self.cte_repo.get_by_id(id)
        prestamos = self.prst_repo.get_by_cte_id(id)

        return cliente, prestamos
        