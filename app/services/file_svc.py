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
        if 'files' not in files:
            return
        
        for i, file in enumerate(files.getlist('files')):
            if not file or file.filename == '':
                continue

            ft_id = form.get(f'fil_ft[{i}]')
            fil_name = form.get(f'fil_name[{i}]')

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

    def process_single_file(self, file, form, cl_id):
        if not file:
            print("No hay archivo")
            return  # No hay archivo válido

        # Obtén los metadatos del formulario (ajusta los nombres según tu formulario)
        ft_id = form.get('fil_ft')  # Sin índice [i]
        fil_name = form.get('fil_name')  # Sin índice [i]

        if not ft_id or not fil_name:
            current_app.logger.warning("Faltan metadatos para el archivo")
            return

        try:
            safe_name = secure_filename(fil_name)
            upload_result = cloudinary.uploader.upload(
                file,
                folder=f"clientes/{cl_id}/",
                public_id=safe_name,
                use_filename=True,
                unique_filename=False,
                resource_type="auto",
            )

            data = {
                'fil_url': upload_result['secure_url'],
                'fil_name': safe_name,
                'ft_id': ft_id,
                'cl_id': cl_id
            }

            self.create(**data)
        except Exception as e:
            current_app.logger.exception("Error subiendo archivo")
            raise  # Opcional: relanza la excepción si necesitas manejarla fuera