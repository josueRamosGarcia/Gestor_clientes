from ..repositories.archivos_repository import ArchivoRepository
from ..utils.helpers import filtrar_datos
from werkzeug.utils import secure_filename
import cloudinary
import cloudinary.uploader
from flask import current_app

class ArchivoServices():
    def __init__(self):
        self.arch_repo = ArchivoRepository()

    def get_file_types(self):
        return self.arch_repo.get_file_types()
        
    def create_archivo(self, **kwargs):
        return self.arch_repo.create(**kwargs)
    
    def procesar_archivos(self, files, form, cte_id):
        if 'archivos' not in files:
            return
        
        for i, file in enumerate(files.getlist('archivos')):
            if not file or file.filename == '':
                continue

            ta_id = form.get(f'archivos_info[{i}][ta_id]')
            arch_nombre = form.get(f'archivos_info[{i}][arch_nombre]')

            if not ta_id or not arch_nombre:
                current_app.logger.warning(f"Faltan metadatos en archivo[{i}]")

            try:
                safe_name = secure_filename(arch_nombre)
                upload_result = cloudinary.uploader.upload(
                    file,
                    folder=f"clientes/{cte_id}/",
                    public_id=safe_name,
                    use_filename=True,
                    unique_filename=False,
                    resource_type="auto",
                )

                datos = filtrar_datos({
                    'arch_url': upload_result['secure_url'],
                    'arch_nombre': safe_name,
                    'ta_id': ta_id,
                    'cte_id': cte_id
                })

                self.arch_service.create_archivo(**datos)
            except Exception as e:
                current_app.logger.exception(f"Error subiendo archivo {i}")
