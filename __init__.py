from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Config')  # configure app using the Config class defined in config.py

    db.init_app(app)  # initialise the database for the app

    with app.app_context():
        db.create_all()

        from home.home import home_bp
        app.register_blueprint(home_bp)

        return app