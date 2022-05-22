from flask import Flask, render_template, request
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime, timedelta
import os
# # import db setup
from app import app
from users import *
from staycation import *
from book import Booking
# import csv 

# This entire page with the Blueprint and MongoEngine library is for question 1) c) 

# link to login/registration page
from auth import auth
app.register_blueprint(auth)

#link to package page
from staycation import package
app.register_blueprint(package)

# link to individual hotel pages
from book import book
app.register_blueprint(book)

# upload of files
def createUsers(email, password, name):
	con = User.objects(email=email).first()
	if not(con):
		User(email=email, password=password, name=name).save()

def createStaycations(hotel_name, duration, unit_cost, image_url, description):
	con = STAYCATION.objects(hotel_name=hotel_name).first()
	if not(con):
		STAYCATION(hotel_name=hotel_name, duration=duration, unit_cost=unit_cost, image_url=image_url, description=description).save()

def createBookings(check_in_date, customer, hname):
	customer = getUserByEmail(customer)
	package = getHotelByHotelName(hname)
	# no requirements for checking of duplicates
	# con = Booking.objects(check_in_date=check_in_date, customer=customer, package=package).first()
	# if not(con):
	booking = Booking(check_in_date=check_in_date, customer=customer, package=package)
	booking.calculate_total_cost()
	booking.save()

''' 
1) b) i) and ii)
For pseudo code reference
set app.route with view '/upload', using methods POST and GET for request
set login required
create function for when page loads for this view
	set title of page
	set string of selected option as empty
	set m of message to display as empty

	if page's request method is POST
		set selected value as the form's input file upload value
		convert lettercase of selected string to lower

		set file path as empty
		set rows as None to instantiate globallay in the function

		set uplf as the files request to retrieve all the files that has been uploaded through the file input
		check first if file input is empty and if true
			set the file path in fpath 
			and then save the path in uplf

			now open the file that is uploaded as thisfile
				set content to be to read the lines of thisfile
			set header to read the first row
			set rows to read the all rows except the first row

		for each row in rows
			set ecr to split by ',' as the delimiter

			check if selected is set to 'users'
				then create users object to be stored into the database
				(function is presented above)
			check if seelct is set to 'staycation'
				then create staycation object to be stored into the database
				(function is presented above)
			check if selected if 'booking'
				then create booking object to be stored into the database
				(function is presented above)

		When all actions are complete, return to rendering page html template using 'upload.html' and including the title variable into the page through the parameter title

'''
@app.route('/upload', methods=['POST','GET'])
@login_required
def uploadform():
	title='Upload'
	selected = ''
	m = ''
	if request.method == 'POST':
		selected = request.form.get('ftype')
		selected = selected.lower()

		fpath = ''
		rows = None
		
		uplf = request.files['file']
		if uplf.filename != '':
			fpath = os.path.join(app.config['UPLOAD_FOLDER'], uplf.filename)
			uplf.save(fpath)

			with open(fpath, 'r') as thisfile:
				content = thisfile.readlines()
			header = content[:1]
			rows = content[1:]
			
		for r in rows:
			ecr = r.split(',')

			if selected == 'users':
				createUsers(ecr[0], ecr[1], ecr[2].replace('"', '').strip())		
			elif selected == 'staycation':
				h = ecr[0].replace('"','')
				createStaycations(h, ecr[1], ecr[2], ecr[3], ecr[4])
			elif selected == 'booking':
				hotel = ecr[2].replace('"', '')
				hotel = hotel.strip()
				createBookings(ecr[0], ecr[1], hotel)
			
	return render_template('upload.html', title=title,)

# link to upload page
from dashboard import tc
app.register_blueprint(tc)

