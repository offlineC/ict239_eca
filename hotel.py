from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask_login import login_required, current_user
from init import db
from bookingform import *
from booking_mod import *
from hotel_mod import *

hotel = Blueprint('hotel',__name__)

@hotel.route('/hotel/<id>', methods=['POST','GET'])
@login_required
def hotelform(id:str):
	thisHotel = getHotelById(id)
	customer = current_user.name
	hotel = thisHotel.hotel_name
	form = bookingf(customer=customer,hotel_name=hotel)
	scmessage = ''
	title = thisHotel.hotel_name
	if request.method == 'GET':
		thisHotel
	if request.method == 'POST':
		scmessage = 'Booking failed'
		if form.validate():
			cid = form.check_in_date.data
			booking = Booking(check_in_date=cid, customer=customer, hotel_name=hotel).save()
			scmessage = 'Booking successful' + str(cid) + customer + hotel
		else:
			scmessage='Unable to validate'
	
	return render_template('hotel.html', title=title, hotel=thisHotel, form=form, scmessage=scmessage)