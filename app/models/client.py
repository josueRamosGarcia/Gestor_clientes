from .base import db
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta    

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

    @property
    def birthdate_curp(self):
        """Extrae la fecha de nacimiento de la CURP"""
        if not self.cl_curp or len(self.cl_curp) < 10:
            return None
            
        fecha_str = self.cl_curp[4:10]
        try:
            # Ajuste para años: 00-99 -> 2000-2099
            year = int(fecha_str[:2]) + (2000 if int(fecha_str[:2]) < 50 else 1900)
            return datetime.strptime(f"{year}{fecha_str[2:]}", "%Y%m%d").date()
        except ValueError:
            return None
        
    @property
    def edad_exacta(self):
        """Calcula la edad en formato 'X años Y meses'"""
        if not self.birthdate_curp:
            return "Fecha no disponible"
            
        hoy = datetime.now(timezone.utc).date()
        delta = relativedelta(hoy, self.birthdate_curp)
        
        # Manejo de plurales
        años = f"{delta.years} año{'s' if delta.years != 1 else ''}"
        meses = f"{delta.months} mes{'es' if delta.months != 1 else ''}"
        
        return f"{años} y {meses}"

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
    cl_obs = db.Column(
        db.String(256)
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
