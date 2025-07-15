from .base import db
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime, timezone

class OperacionAuditoria(db.Model):
    __tablename__ = 'operaciones_auditoria'

    op_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    op_nombre = db.Column(
        db.String(32),
        nullable=False
    )

    eventos = db.relationship(
        'EventoAuditoria',
        back_populates='operacion'
    )

    def __repr__(self):
        return f"{self.op_id} - {self.op_nombre}"

class EventoAuditoria(db.Model):
    __tablename__ = 'eventos_auditoria'

    adt_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    adt_tabla = db.Column(
        db.String(64),
        nullable=False
    )
    adt_fecha = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
    adt_dat_ant = db.Column(
        JSONB
    )
    adt_dat_des = db.Column(
        JSONB
    )
    adt_ip = db.Column(
        db.String(45),
        nullable=False
    )
    op_id = db.Column(
        db.Integer,
        db.ForeignKey('operaciones_auditoria.op_id'),
        nullable=False
    )
    usr_id = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.usr_id'),
        nullable=False
    )

    operacion = db.relationship(
        'OperacionAuditoria',
        back_populates='eventos'
    )
    usuario = db.relationship(
        'Usuario',
        back_populates='eventos'
    )

    def __repr__(self):
        return (
            f"{self.adt_id} - {self.adt_tabla} - {self.adt_fecha} - "
            f"{self.adt_ip} - {self.op_id} - {self.usr_id}"
        )
