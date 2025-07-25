from ..repositories.prestamo_repository import PrestamoRepository

class PrestamoService:
    def __init__(self):
        self.prst_repo = PrestamoRepository()

    def __getattr__(self, name):
        return getattr(self.prst_repo, name)