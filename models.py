from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime, timezone

db = SQLAlchemy()

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
            
    
class EstatusPrestamo(db.Model):
    __tablename__ = 'estatus_prestamos'

    ep_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    ep_nombre = db.Column(
        db.String(32),
        nullable=False
    )

    prestamos = db.relationship(
        'Prestamo',
        back_populates='estatus'
    )

    def __repr__(self):
        return f"{self.ep_id} - {self.ep_nombre}"
    
class TipoPrestamo(db.Model):
    __tablename__ = 'tipos_prestamos'

    tp_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    tp_nombre = db.Column(
        db.String(32),
        nullable=False
    )

    prestamos = db.relationship(
        'Prestamo',
        back_populates='tipo'
    )

    def __repr__(self):
        return f"{self.tp_id} - {self.tp_nombre}"

class Prestamo(db.Model):
    __tablename__ = 'prestamos'

    prst_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    prst_financiera = db.Column(
        db.String(32),
        nullable=False
    )
    prst_cat = db.Column(
        db.Numeric(5,2),
        nullable=False
    )
    prst_monto = db.Column(
        db.Numeric(8,2),
        nullable=False
    )
    prst_descuento = db.Column(
        db.Numeric(7,2),
        nullable=False
    )
    prst_plazo = db.Column(
        db.Integer,
        nullable=False
    )
    prst_imp_pagar = db.Column(
        db.Numeric(8,2),
        nullable=False
    )
    prst_f_p_desc = db.Column(
        db.Date,
        nullable=False
    )
    prst_id_liq = db.Column(
        db.Integer
    )
    cte_id = db.Column(
        db.Integer,
        db.ForeignKey('clientes.cte_id'),
        nullable=False
    )
    tp_id = db.Column(
        db.Integer,
        db.ForeignKey('tipos_prestamos.tp_id'),
        nullable=False
    )
    ep_id = db.Column(
        db.Integer,
        db.ForeignKey('estatus_prestamos.ep_id'),
        nullable=False
    )

    cliente = db.relationship(
        'Cliente',
        back_populates='prestamos'
    )
    tipo = db.relationship(
        'TipoPrestamo',
        back_populates='prestamos'
    )
    estatus = db.relationship(
        'EstatusPrestamo',
        back_populates='prestamos'
    )

    def __repr__(self):
        return (
            f"{self.prst_id} - {self.prst_financiera} - {self.prst_cat} - "
            f"{self.prst_monto} - {self.prst_descuento} - "
            f"{self.prst_plazo} - {self.prst_imp_pagar} - "
            f"{self.prst_f_p_desc} - {self.prst_id_liq} - "
            f"{self.cte_id} - {self.tp_id} - {self.ep_id}"
        )

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
    