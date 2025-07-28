from ..repositories.user_repo import UserRepository
from werkzeug.security import check_password_hash
from ..utils.helpers import get_usr_id_log

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def get_logged_user(self):
        usr_id = get_usr_id_log()

        if usr_id:
            return self.user_repo.get_by_id(usr_id)
        return None

    def authenticate_user(self, username, password):
        user = self.user_repo.get_by_username(username)

        if not user:
            return None, "Usuario no encontrado"
        if not user.usr_is_active:
            return None, "Usuario no activo"
        if not check_password_hash(user.usr_password, password):
            return None, "Contraseña incorrectas"
        return user, None
