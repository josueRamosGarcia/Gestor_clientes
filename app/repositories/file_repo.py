from .base_repo import BaseRepository
from ..models.file import File, FileType

class FileRepository(BaseRepository):
    def __init__(self):
        super().__init__(File)
        self.id_field = 'fil_id'

    def get_file_types(self):
        return self.db.session.query(FileType).all()
