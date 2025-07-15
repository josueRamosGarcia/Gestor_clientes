from .base import db

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