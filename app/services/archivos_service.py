from ..repositories.archivos_repository import ArchivoRepository

class ArchivoServices():
    def __init__(self):
        self.arch_repo = ArchivoRepository()

    def get_file_types(self):
        return self.arch_repo.get_file_types()
        