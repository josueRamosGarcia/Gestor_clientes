from ..repositories.usuario_repository import UsuarioRepository
from werkzeug.security import check_password_hash
from ..utils.helpers import get_usr_id_log

class AuthService:
    def __init__(self):
        self.usr_repo = UsuarioRepository()

    def get_logged_user(self):
        
        user_id = get_usr_id_log()

        if user_id:
            return self.usr_repo.get_by_id(user_id)
        return None

    def authenticate_user(self, username, password):
        user = self.usr_repo.get_by_username(username)

        if not user:
            return None, "Usuario no encontrado"
        if not user.usr_activo:
            return None, "Usuario no activo"
        if not check_password_hash(user.usr_pass, password):
            return None, "Contraseña incorrectas"

        return user, None