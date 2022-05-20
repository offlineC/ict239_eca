from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from users import *
from app import db 
from staycation import *
from forms import bookForm
from datetime import datetime as dt
from datetime import timedelta

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

def getAllBookings():
	bookings = Booking.objects()
	return bookings

def dataOutput():
	data = getAllBookings()
	startDate = dt(2022,1,17)
	endDate = dt(2022,3,12)
	hnames = []
	inData = {}
	# inData['dates'] = [(startDate+timedelta(x)).date() for x in range((endDate-startDate).days)]
	inData['hotels'] = []

	for h in data:
		print(h.package)
		# if not( h in hnames):
		# 	hone = h
		# 	hnames.append(hone)

	# for i in hnames:
	# 	thisHotel = getHotelByHotelName(i)
	# 	dates = [str(n['check_in_date']) for n in data if n['hotel_name'] == i]
	# 	dates.sort()
	# 	price = thisHotel['unit_cost']*thisHotel['duration']
	# 	inData['hotels'].append({'name':i, 'price':price, 'dates': dates, 'perDay':[]})

	
	# for d in inData['hotels']:
	# 	for ds in d['dates']:
	# 		dcount = d['dates'].count(ds)
	# 		dayself = dt.strptime(ds, '%Y-%m-%d')
	# 		dateDic = {str(ds):dcount}
	# 		if not(dateDic in d['perDay']):
	# 			d['perDay'].append(dateDic)


	return inData

book = Blueprint('book',__name__)

@book.route('/booking/<id>', methods=['POST','GET'])
@login_required
def hotelform(id:str):
	thisHotel = getHotelById(id)
	customer = getUserDataById(current_user.id)
	package = getHotelDataById(id)
	total_cost = package['unit_cost'] * package['duration']
	form = bookForm()
	scmessage = ''
	title = thisHotel.hotel_name
	if request.method == 'GET':
		thisHotel
	if request.method == 'POST':
		scmessage = 'Booking failed'
		if form.validate():
			cid = form.check_in_date.data
			booking = Booking(check_in_date=cid, customer=customer, package=package, total_cost = total_cost).save()
			scmessage = 'Booking successful' + str(cid) + str(customer) +str(package)
		else:
			scmessage='Unable to validate'
	
	return render_template('booking.html', title=title, hotel=thisHotel, form=form, scmessage=scmessage)