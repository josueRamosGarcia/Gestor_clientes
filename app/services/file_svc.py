from ..repositories.file_repo import FileRepository
from ..utils.helpers import filter_data
from werkzeug.utils import secure_filename
import cloudinary
import cloudinary.uploader
from flask import current_app

class FileService():
    def __init__(self):
        self.file_repo = FileRepository()

    def __getattr__(self, name):
        return getattr(self.file_repo, name)
    
    def process_files(self, files, form, cl_id):
        if 'archivos' not in files:
            return
        
        for i, file in enumerate(files.getlist('archivos')):
            if not file or file.filename == '':
                continue

            ft_id = form.get(f'archivos_info[{i}][ta_id]')
            fil_name = form.get(f'archivos_info[{i}][arch_nombre]')

            if not ft_id or not fil_name:
                current_app.logger.warning(f"Faltan metadatos en archivo[{i}]")

            try:
                safe_name = secure_filename(fil_name)
                upload_result = cloudinary.uploader.upload(
                    file,
                    folder = f"clientes/{cl_id}/",
                    public_id = safe_name,
                    use_filename = True,
                    unique_filename = False,
                    resource_type = "auto",
                )

                data = filter_data({
                    'fil_url': upload_result['secure_url'],
                    'fil_name': safe_name,
                    'ft_id': ft_id,
                    'cl_id': cl_id
                })

                self.create(**data)
            except Exception as e:
                current_app.logger.exception(f"Error subiendo archivo {i}")
