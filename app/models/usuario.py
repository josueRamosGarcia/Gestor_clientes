from .base import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    usr_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    usr_nombre = db.Column(
        db.String(64),
        nullable=False
    )
    usr_username = db.Column(
        db.String(32),
        nullable=False,
        unique=True
    )
    usr_pass = db.Column(
        db.String(256),
        nullable=False
    )
    usr_activo = db.Column(
        db.Boolean,
        default=True
    )

    eventos = db.relationship(
        'EventoAuditoria',
        back_populates='usuario'
    )

    def __repr__(self):
        return (
            f"{self.usr_id} - {self.usr_nombre} - "
            f"{self.usr_username} - {self.usr_activo}"
        )
