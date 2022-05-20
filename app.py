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
	customer = getUserDataByEmail(customer)
	package = getHotelDataByHotelName(hname)
	# no requirements for checking of duplicates
	# con = Booking.objects(check_in_date=check_in_date, customer=customer, package=package).first()
	# if not(con):
	total_cost = package['unit_cost'] * package['duration']
	Booking(check_in_date=check_in_date, customer=customer, package=package, total_cost=total_cost).save()

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
				createUsers(ecr[0], ecr[1], ecr[2])		
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

