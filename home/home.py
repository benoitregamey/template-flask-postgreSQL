from flask import Blueprint, render_template
from models import db, metadata

home_bp = Blueprint('home', __name__, template_folder='templates',
    static_folder='static')

@home_bp.route('/')
def index():
    return render_template('index.html', metadata=db.session.query(metadata).all())