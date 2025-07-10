from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ENUM, JSONB
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

    def __repr__(self):
        return (
            f"{self.cte_id} - {self.cte_nombre} - {self.cte_apellidos} - "
            f"{self.cte_curp} - {self.cte_nss} - {self.cte_rfc} - "
            f"{self.ec_id} - {self.corr_id}"
        )
    
class Telefono(db.model):
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
        db.String(100),
        nullable=False
    )
    tel_parentesco = db.Column(
        db.String(64),
        nullable=False
    )
    cte_id = db.Column(
        db.Integer,
        db.ForeigKey('clientes.cte_id'),
        nullable=False
    )

    cliente = db.relationship(
        'clientes',
        backref='telefonos'
    )

    def __repr__(self):
        return (
            f"{self.tel_id} - {self.tel_telefono} - {self.tel_nombre} - "
            f"{self.tel_parentesco} - {self.cte_id}"
        )
            
    
class Estatus_prestamo(db.model):
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

    def __repr__(self):
        return f"{self.ep_id} - {self.ep_nombre}"
    
class Tipo_prestamo(db.model):
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

    def __repr__(self):
        return f"{self.tp_id} - {self.tp_nombre}"

class Prestamo(db.model):
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
        db.ForeignKey('estatus_prestamo.ep_id')
    )

    cliente = db.relationship(
        'clientes',
        backref='prestamos'
    )
    tipo_prestamo = db.relatrionship(
        'tipos_prestamos',
        backref='prestamos'
    )
    estatus_prestamo = db.relationship(
        'estatus_prestamos',
        backref='prestamos'
    )

    def __repr__(self):
        return (
            f"{self.prst_id} - {self.prst_financiera} - {self.prst_cat} - "
            f"{self.prst_monto} - {self.prst_descuento} - "
            f"{self.prst_plazo} - {self.prst_imp_pagar} - "
            f"{self.prst_f_p_desc} - {self.prst_id_liq} - "
            f"{self.cte_id} - {self.tp_id} - {self.ep_id}"
        )

class Usuario(db.model):
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

    def __repr__(self):
        return (
            f"{self.usr_id} - {self.usr_nombre} - "
            f"{self.usr_username} - {self.usr_activo}"
        )

class Operacion_auditoria(db.model):
    __tablename__ = 'operaciones_auditoria'

    op_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    op_nombre = db.Column(
        db.String(32),
        nulleable=False
    )

    def __repr__(self):
        return f"{self.op_id} - {self.op_nombre}"

class Evento_auditoria(db.model):
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

    operacion_auditoria = db.relationship(
        'operaciones_auditoria',
        backref='eventos_auditoria'
    )
    usuario = db.relationship(
        'usuarios',
        backref='eventos_auditorias'
    )

    def __repr__(self):
        return (
            f"{self.adt_id} - {self.adt_tabla} - {self.adt_oper} - "
            f"{self.adt_fecha} - {self.adt_ip} - {self.usr_id}"
        )

class Tipo_archivo(db.model):
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
        nulleable=False
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

    tipo_archivo = db.relationship(
        'tipos_archivos',
        backref='archivos'
    )
    cliente = db.relationship(
        'clientes',
        backref='archivos'
    )

    def __repr__(self):
        return (
            f"{self.arch_id} - {self.arch_url} - {self.arch_nombre} - "
            f"{self.arch_f_subida} - {self.ta_id} - {self.cte_id}"
        )
    