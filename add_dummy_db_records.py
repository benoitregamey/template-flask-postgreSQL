import uuid
from __init__ import create_app
from models import db, metadata

app = create_app()

with app.app_context():
        for i in range(1000):
            row = metadata(id=uuid.uuid4(), title=f"test-{i}", published=True, valid=True)
            db.session.add(row)
            db.session.commit()
