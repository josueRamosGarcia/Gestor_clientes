from abc import ABC
from config.database import db

class BaseRepository(ABC):
    def __init__(self, model):
        self.model = model
        self.db = db
        self.id_field = "id"

    def get_all(self):
        return self.db.session.query(self.model).all()
    
    def get_by_id(self, id):
        return self.db.session.query(self.model).filter_by(
            **{self.id_field: id}
        ).first()

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        self.db.session.add(instance)
        self.db.session.commit()
        return instance
    
    def update(self, id, **kwargs):
        instance = self.get_by_id(id)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            self.db.session.commit()
        return instance
    
    def delete(self, id):
        instance = self.get_by_id(id)
        if instance:
            self.db.session.delete(instance)
            self.db.session.commit()
        return instance    
