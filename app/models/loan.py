from .base import db
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta 

class FinancialInstitucion(db.Model):
    __tablename__ = 'financial_institutions'

    fi_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    fi_name = db.Column(
        db.String(32),
        nullable = False
    )

    loans = db.relationship(
        'Loan',
        back_populates = 'financial_institution'
    )

class LoanStatus(db.Model):
    __tablename__ = 'loan_status'

    ls_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    ls_name = db.Column(
        db.String(32),
        nullable = False
    )

    loans = db.relationship(
        'Loan',
        back_populates = 'loan_status'
    )

class LoanType(db.Model):
    __tablename__ = 'loan_types'

    lt_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    lt_name = db.Column(
        db.String(32),
        nullable = False
    )

    loans = db.relationship(
        'Loan',
        back_populates = 'loan_type'
    )

class Loan(db.Model):
    __tablename__ = 'loans'

    @property
    def months_since_first_discount(self):
        """
        Calcula los meses transcurridos desde la fecha de primer descuento.
        Retorna 0 si no hay fecha definida.
        """
        # 1. Verificamos si existe la fecha
        if not self.ln_f_disc_dt:
            return 0
            
        # 2. Obtenemos la fecha actual (UTC para consistencia)
        current_date = datetime.now(timezone.utc).date()
        
        # 3. Calculamos la diferencia usando relativedelta (más preciso que días/30)
        delta = relativedelta(current_date, self.ln_f_disc_dt)
        
        # 4. Convertimos años a meses y sumamos los meses restantes
        return delta.years * 12 + delta.months + 1

    ln_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    ln_cat = db.Column(
        db.Numeric(5,2),
        nullable = False
    )
    ln_amount = db.Column(
        db.Numeric(8,2),
        nullable = False
    )
    ln_discount = db.Column(
        db.Numeric(7,2),
        nullable = False
    )
    ln_term = db.Column(
        db.Integer,
        nullable = False
    )
    ln_am_pay = db.Column(
        db.Numeric(8,2),
        nullable = False
    )
    ln_f_disc_dt = db.Column(
        db.Date,
        nullable = False
    )
    ln_liq_id = db.Column(
        db.Integer
    )
    cl_id = db.Column(
        db.Integer,
        db.ForeignKey('clients.cl_id'),
        nullable = False
    )
    fi_id = db.Column(
        db.Integer,
        db.ForeignKey('financial_institutions.fi_id'),
        nullable = False
    )
    ls_id = db.Column(
        db.Integer,
        db.ForeignKey('loan_status.ls_id'),
        nullable = False
    )
    lt_id = db.Column(
        db.Integer,
        db.ForeignKey('loan_types.lt_id'),
        nullable = False
    )

    client = db.relationship(
        'Client',
        back_populates = 'loans'
    )
    financial_institution = db.relationship(
        'FinancialInstitucion',
        back_populates = 'loans'
    )
    loan_type = db.relationship(
        'LoanType',
        back_populates = 'loans'
    )
    loan_status = db.relationship(
        'LoanStatus',
        back_populates = 'loans'
    )
