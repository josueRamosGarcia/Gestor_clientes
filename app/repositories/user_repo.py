from .base_repo import BaseRepository
from ..models.user import User

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
        self.id_field = "usr_id"

    def get_by_username(self, username):
        return self.db.session.query(User).filter_by(
            usr_username = username
        ).first()