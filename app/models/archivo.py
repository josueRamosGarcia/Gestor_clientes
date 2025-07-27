from .base import db
from datetime import datetime, timezone

class FileType(db.Model):
    __tablename__ = 'file_types'
    
    ft_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    ft_name = db.Column(
        db.String(32),
        nullable = False
    )

    files = db.relationship(
        'File',
        back_populates = 'file_type'
    )

class File(db.Model):
    __tablename__ = 'files'

    fil_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    fil_url = db.Column(
        db.Text,
        nullable = False
    )
    fil_name = db.Column(
        db.String(64),
        nullable = False
    ) 
    fil_up_dt = db.Column(
        db.DateTime(timezone = True),
        default = lambda: datetime.now(timezone.utc)
    )
    ft_id = db.Column(
        db.Integer,
        db.ForeignKey('file_types.ft_id'),
        nullable = False
    )
    cl_id = db.Column(
        db.Integer,
        db.ForeignKey('clients.cl_id'),
        nullable = False
    )

    file_type = db.relationship(
        'FileType',
        back_populates='files'
    )
    client = db.relationship(
        'Client',
        back_populates='files'
    )
