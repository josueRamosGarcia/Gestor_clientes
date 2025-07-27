from .base import db

class User(db.Model):
    __tablename__ = 'users'

    usr_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    usr_name = db.Column(
        db.String(64),
        nullable = False
    )
    usr_username = db.Column(
        db.String(32),
        nullable = False,
        unique = True
    )
    usr_password = db.Column(
        db.String(256),
        nullable = False
    )
    usr_is_active = db.Column(
        db.Boolean,
        default = True
    )

    audit_events = db.relationship(
        'AuditEvent',
        back_populates = 'user'
    )

