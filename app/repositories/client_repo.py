from .base_repo import BaseRepository
from ..models.client import Client, ClientStatus, Email, PhoneNumber

class ClientRepository(BaseRepository):
    def __init__(self):
        super().__init__(Client)
        self.id_field = "cl_id"

    # --- Client Methods ---
    def search_by_name(self, search):
        return self.db.session.query(self.model).filter(
            self.db.or_(
                self.model.cl_name.ilike(f"%{search}%"),
                self.model.cl_lname.ilike(f"%{search}%")
            )
        ).order_by(self.model.cl_name, self.model.cl_lname).all()

    def get_client_id_by_curp(self, curp):
        return self.db.session.query(self.model.cl_id).filter_by(
            cl_curp = curp
        ).first() 
    
    def get_status(self):
        return self.db.session.query(ClientStatus).all()
    
    # --- Email Methods ---
    def create_email(self,**kwargs):
        instance = Email(**kwargs)
        self.db.session.add(instance)
        self.db.session.commit()
        return instance
    
    def get_email_id_by_name(self, name):
        return self.db.session.query(Email.em_id).filter_by(
            em_name = name
        ).first()
    
    # --- Phone Number Methods ---
    def create_phone_number(self, **kwargs):
        instance = PhoneNumber(**kwargs)
        self.db.session.add(instance)
        self.db.session.commit()
        return instance
