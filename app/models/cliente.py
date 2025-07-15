from .base import db

class EstatusCliente(db.Model):
    __tablename__ = 'estatus_clientes'

    ec_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    ec_nombre = db.Column(
        db.String(32),
        nullable=False
    )

    clientes = db.relationship(
        'Cliente',
        back_populates='estatus'
    )

    def __repr__(self):
        return f"{self.ec_id} - {self.ec_nombre}"

class Correo(db.Model):
    __tablename__ = 'correos'

    corr_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    corr_nombre = db.Column(
        db.String(64),
        nullable=False,
        unique=True
    )
    corr_contraseña = db.Column(
        db.String(256)
    )
    corr_localizacion = db.Column(
        db.String(64)
    )

    cliente = db.relationship(
        'Cliente',
        back_populates='correo',
        uselist=False
    )

    def __repr__(self):
        return (
            f"{self.corr_id} - {self.corr_nombre} - "
            f"{self.corr_localizacion}"
        )

class Cliente(db.Model):
    __tablename__ = 'clientes'

    cte_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    cte_nombre = db.Column(
        db.String(64),
        nullable=False
    )
    cte_apellidos = db.Column(
        db.String(64),
        nullable=False
    )
    cte_curp = db.Column(
        db.String(18),
        nullable=False,
        unique=True
    )
    cte_nss = db.Column(
        db.String(11),
        nullable=False,
        unique=True
    )
    cte_rfc = db.Column(
        db.String(13),
        unique=True
    )
    ec_id = db.Column(
        db.Integer,
        db.ForeignKey('estatus_clientes.ec_id'),
        nullable=False
    )
    corr_id = db.Column(
        db.Integer,
        db.ForeignKey('correos.corr_id'),
        unique=True
    )

    estatus = db.relationship(
        'EstatusCliente',
        back_populates='clientes'
    )
    correo = db.relationship(
        'Correo',
        back_populates='cliente'
    )
    telefonos = db.relationship(
        'Telefono',
        back_populates='cliente'
    )
    prestamos = db.relationship(
        'Prestamo',
        back_populates='cliente'
    )
    archivos = db.relationship(
        'Archivo',
        back_populates='cliente'
    )

    def __repr__(self):
        return (
            f"{self.cte_id} - {self.cte_nombre} - {self.cte_apellidos} - "
            f"{self.cte_curp} - {self.cte_nss} - {self.cte_rfc} - "
            f"{self.ec_id} - {self.corr_id}"
        )
    
class Telefono(db.Model):
    __tablename__ = 'telefonos'

    tel_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    tel_telefono = db.Column(
        db.String(10),
        nullable=False
    )
    tel_nombre = db.Column(
        db.String(128),
        nullable=False
    )
    tel_parentesco = db.Column(
        db.String(64),
        nullable=False
    )
    cte_id = db.Column(
        db.Integer,
        db.ForeignKey('clientes.cte_id'),
        nullable=False
    )

    cliente = db.relationship(
        'Cliente',
        back_populates='telefonos'
    )

    def __repr__(self):
        return (
            f"{self.tel_id} - {self.tel_telefono} - {self.tel_nombre} - "
            f"{self.tel_parentesco} - {self.cte_id}"
        )
