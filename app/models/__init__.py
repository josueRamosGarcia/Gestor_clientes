# Importar imstancia de base de datos
from .base import db

# Importar modelos
from .archivo import TipoArchivo, Archivo
from .auditoria import OperacionAuditoria, EventoAuditoria
from .cliente import EstatusCliente, Correo, Cliente, Telefono
from .prestamo import TipoPrestamo, EstatusPrestamo, Prestamo
from .usuario import Usuario

__all__ = [
    'db',
    'TipoArchivo',
    'Archivo',
    'OperacionAuditoria',
    'EventoAuditoria',
    'EstatusCliente',
    'Correo',
    'Cliente',
    'Telefono',
    'TipoPrestamo',
    'EstatusPrestamo',
    'Prestamo',
    'Usuario'
]
