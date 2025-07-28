"""
Módulo de repositorios para acceso a datos.
Contiene implementaciones base y específicas de repositorios.
"""

from .client_repo import ClientRepository
from .loan_repo import LoanRepository
from .file_repo import FileRepository
from .user_repo import UserRepository

__all__ = [
    'ClientRepository',
    'LoanRepository',
    'FileRepository',
    'UserRepository'
]