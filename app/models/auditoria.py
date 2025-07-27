from .base import db
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime, timezone

class AuditOperation(db.Model):
    __tablename__ = 'audit_operations'

    op_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    op_name = db.Column(
        db.String(32),
        nullable = False
    )

    audit_event = db.relationship(
        'AuditEvent',
        back_populates = 'audit_operation'
    )

class AuditEvent(db.Model):
    __tablename__ = 'audit_events'

    ev_id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    ev_table = db.Column(
        db.String(64),
        nullable = False
    )
    ev_date = db.Column(
        db.DateTime(timezone = True),
        default = lambda: datetime.now(timezone.utc)
    )
    ev_bef_data = db.Column(
        JSONB
    )
    ev_aft_data = db.Column(
        JSONB
    )
    ev_ip = db.Column(
        db.String(45),
        nullable = False
    )
    op_id = db.Column(
        db.Integer,
        db.ForeignKey('audit_operations.op_id'),
        nullable = False
    )
    usr_id = db.Column(
        db.Integer,
        db.ForeignKey('users.usr_id'),
        nullable = False
    )

    operation = db.relationship(
        'AuditOperation',
        back_populates = 'audit_events'
    )
    user = db.relationship(
        'User',
        back_populates = 'audit_events'
    )
