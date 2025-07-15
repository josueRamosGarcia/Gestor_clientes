from .base_repository import BaseRepository
from models.usuario import Usuario

class UsuarioRepository(BaseRepository):
    def __init__(self):
        super().__init__(Usuario)
        self.id_field = "usr_id"

    def get_by_username(self, username):
        return self.db.session.query(Usuario).filter_by(
            usr_username = username
        ).firs()