from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()

class metadata(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(250), unique=False, nullable=False)
    published = db.Column(db.Boolean, nullable=False)
    valid = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<metadata %r>' % self.title