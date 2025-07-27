from .base import db

class ClientStatus(db.Model):
    __tablename__ = 'client_status'

    cs_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    cs_name = db.Column(
        db.String(32),
        nullable = False
    )

    clients = db.relationship(
        'Client',
        back_populates = 'client_status'
    )

class Email(db.Model):
    __tablename__ = 'emails'

    em_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    em_name = db.Column(
        db.String(64),
        nullable = False,
        unique = True
    )
    em_password = db.Column(
        db.String(256)
    )
    em_location = db.Column(
        db.String(64)
    )

    client = db.relationship(
        'Client',
        back_populates = 'email',
        uselist = False
    )

class Client(db.Model):
    __tablename__ = 'clients'

    cl_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    cl_name = db.Column(
        db.String(64),
        nullable = False
    )
    cl_lname = db.Column(
        db.String(64),
        nullable = False
    )
    cl_curp = db.Column(
        db.String(18),
        nullable = False,
        unique = True
    )
    cl_nss = db.Column(
        db.String(11),
        nullable = False,
        unique = True
    )
    cl_rfc = db.Column(
        db.String(13),
        nullable = False,
        unique = True
    )
    cs_id = db.Column(
        db.Integer,
        db.ForeignKey('client_status.cs_id'),
        nullable = False
    )
    em_id = db.Column(
        db.Integer,
        db.ForeignKey('emails.em_id'),
        unique = True
    )

    client_status = db.relationship(
        'ClientStatus',
        back_populates = 'clients'
    )
    email = db.relationship(
        'Email',
        back_populates = 'client'
    )
    phone_numbers = db.relationship(
        'PhoneNumber',
        back_populates = 'client'
    )
    loans = db.relationship(
        'Loan',
        back_populates = 'client'
    )
    files = db.relationship(
        'File',
        back_populates = 'client'
    )

class PhoneNumber(db.Model):
    __tablename__ = 'phone_numbers'

    ph_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    ph_number = db.Column(
        db.String(10),
        nullable = False
    )
    ph_name = db.Column(
        db.String(128),
        nullable = False
    )
    ph_rel = db.Column(
        db.String(64),
        nullable = False
    )
    cl_id = db.Column(
        db.Integer,
        db.ForeignKey('clients.cl_id'),
        nullable = False
    )

    client = db.relationship(
        'Client',
        back_populates = 'phone_numbers'
    )
