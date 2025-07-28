from .base_repo import BaseRepository
from ..models.loan import Loan, LoanStatus, LoanType, FinancialInstitucion

class LoanRepository(BaseRepository):
    def __init__(self):
        super().__init__(Loan)
        self.id_field = "ln_id"

    def get_by_cl_id(self, cl_id):
        return self.db.session.query(self.model).filter_by(
            cl_id = cl_id
        ).all()

    def get_status(self):
        return self.db.session.query(LoanStatus).all()
    
    def get_types(self):
        return self.db.session.query(LoanType).all()
    
    def get_financial_institutions(self):
        return self.db.session.query(FinancialInstitucion).all()