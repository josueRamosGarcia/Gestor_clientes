from .base_repository import BaseRepository
from ..models.archivo import Archivo, TipoArchivo

class ArchivoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Archivo)

        self.id_field = 'arch_id'

    def get_file_types(self):
        return self.db.session.query(TipoArchivo).all()

