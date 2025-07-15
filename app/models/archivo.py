from .base import db
from datetime import datetime, timezone

class TipoArchivo(db.Model):
    __tablename__ = 'tipos_archivos'
    
    ta_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    ta_nombre = db.Column(
        db.String(32),
        nullable=False
    )

    archivos = db.relationship(
        'Archivo',
        back_populates='tipo'
    )

    def __repr__(self):
        return f"{self.ta_id} - {self.ta_nombre}"

class Archivo(db.Model):
    __tablename__ = 'archivos'

    arch_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    arch_url = db.Column(
        db.Text,
        nullable=False
    )
    arch_nombre = db.Column(
        db.String(64),
        nullable=False
    ) 
    arch_f_subida = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
    ta_id = db.Column(
        db.Integer,
        db.ForeignKey('tipos_archivos.ta_id'),
        nullable=False
    )
    cte_id = db.Column(
        db.Integer,
        db.ForeignKey('clientes.cte_id'),
        nullable=False
    )

    tipo = db.relationship(
        'TipoArchivo',
        back_populates='archivos'
    )
    cliente = db.relationship(
        'Cliente',
        back_populates='archivos'
    )

    def __repr__(self):
        return (
            f"{self.arch_id} - {self.arch_url} - {self.arch_nombre} - "
            f"{self.arch_f_subida} - {self.ta_id} - {self.cte_id}"
        )
