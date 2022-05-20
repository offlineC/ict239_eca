from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from users import User
from app import db 
from staycation import STAYCATION

class Booking(db.Document):
	# 1) a)
	# Sets up the name of the collection
	meta = {'collection': 'booking'}
	# Creates a check in date field/column in the collection of book as data type datetime
	check_in_date = db.DateTimeField(required=True)
	# Creates a customer field/column in the collection of book that REFERENCES the user collection
	customer = db.ReferenceField(User)
	# Creates a package field/column in the collection of book that REFERENCES the staycation collection
	package = db.ReferenceField(STAYCATION)
	# Creates a total cost field/column in the collection of book as data type float
	total_cost = db.FloatField()

	# Calculates the total cost of each package with its own unit_cost multiplied by its own duration. When this method is called, it just returns the value of the total cost.
	def calculate_total_cost(self):
		self.total_cost = self.package.duration * self.package.unit_cost

book = Blueprint('book',__name__)

@book.route('/hotel/<id>', methods=['POST','GET'])
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