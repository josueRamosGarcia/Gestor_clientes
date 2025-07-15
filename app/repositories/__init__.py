"""
Módulo de repositorios para acceso a datos.
Contiene implementaciones base y específicas de repositorios.
"""

from .cliente_repository import ClienteRepository
from .prestamo_repository import PrestamoRepository

__all__ = [
    'ClienteRepository',
    'PrestamoRepository'
]