from flask import Blueprint, render_template, abort, flash, redirect, url_for, request
from flask_login import login_required, current_user
views = Blueprint('views', __name__)
from Website.models import db, User, Bungalow, Bungalowtype, Reservation
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


@views.route('/')
@login_required
def home():
    bungalows = Bungalow.query.all()
    return render_template("home.html", user=current_user, bungalows=bungalows)

@views.route('/booking/<int:id>')
@login_required
def booking(id):
    bungalow = Bungalow.query.get(id)

    if bungalow:
        return render_template('booking.html', user=current_user, bungalow=bungalow)
    else:
        abort(404, description="Bungalow not found")

@views.route('/reservations/')
@login_required
def reservation():
    return render_template('reservations.html', user=current_user)

@views.route('/booking/<int:id>/reservation', methods=['POST'])
@login_required
def create_reservation(id):
    # Check if the user has already made a reservation for this bungalow
    existing_reservation = Reservation.query.filter_by(user_id=current_user.id, bungalow_id=id).first()
    if existing_reservation:
        flash('You have already made a reservation for this bungalow.', category='error')
    else:
        # Create a new reservation
        reservation = Reservation(user_id=current_user.id, bungalow_id=id, week=request.form.get('week'))
        db.session.add(reservation)
        db.session.commit()
        flash('Reservation created successfully.', category='succes')

    return redirect(url_for('views.booking',user=current_user, id=id))