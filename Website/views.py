from flask import Blueprint, render_template
from flask_login import login_required, current_user
views = Blueprint('views', __name__)
from Website.models import Bungalow, Bungalowtype

@views.route('/')
@login_required
def home():
    bungalows = Bungalow.query.all()
    return render_template("home.html", user=current_user, bungalows=bungalows)