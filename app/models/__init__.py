# Importar imstancia de base de datos
from .base import db

# Importar modelos
from .file import File, FileType
from .audit import AuditEvent, AuditOperation
from .client import Client, ClientStatus, Email, PhoneNumber
from .loan import Loan, LoanStatus, LoanType
from .user import User

__all__ = [
    'db',
    'File',
    'FileType',
    'AuditEvent',
    'AuditOperation',
    'Client',
    'ClientStatus',
    'Email',
    'PhoneNumber',
    'Loan',
    'LoanType',
    'LoanStatus',
    'User'
]
