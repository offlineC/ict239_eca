# from flask import Flask, render_template, request
# from flask_login import login_user, login_required, logout_user, current_user
# from datetime import datetime, timedelta
# # import db setup
from app import app
from users import User
# import csv 


# link to login/registration page
from auth import auth
app.register_blueprint(auth)

# #link to package page
# from staycation import package
# app.register_blueprint(package)

# # link to individual hotel pages
# from book import book
# app.register_blueprint(book)

# # upload of files
# import staycation
# import users
# import book
# def createUsers(email, password, name):
# 	con = User.objects(email=email).first()
# 	if not(con):
# 		User(email=email, password=password, name=name).save()

# def createStaycations(hotel_name, duration, unit_cost, image_url, description):
# 	con = Hotel.objects(hotel_name=hotel_name).first()
# 	if not(con):
# 		Hotel(hotel_name=hotel_name, duration=duration, unit_cost=unit_cost, image_url=image_url, description=description).save()

# def createBookings(check_in_date, customer, hotel_name):
# 	con = Booking.objects(check_in_date=check_in_date, customer=customer, hotel_name=hotel_name).first()
# 	if not(con):
# 		Booking(check_in_date=check_in_date, customer=customer, hotel_name=hotel_name).save()

# @app.route('/upload', methods=['POST','GET'])
# @login_required
# def uploadform():
# 	title='Upload'
# 	selected = ''
# 	m = ''
# 	if request.method == 'POST':
# 		selected = request.form.get('ftype')
# 		selected = selected.lower()

# 		fpath = ''
# 		rows = None
		
# 		uplf = request.files['file']
# 		if uplf.filename != '':
# 			fpath = os.path.join(app.config['UPLOAD_FOLDER'], uplf.filename)
# 			uplf.save(fpath)

# 			with open(fpath, 'r') as thisfile:
# 				content = thisfile.readlines()
# 			header = content[:1]
# 			rows = content[1:]
			
# 		for r in rows:
# 			ecr = r.split(',')

# 			if selected == 'users':
# 				createUsers(ecr[0], ecr[1], ecr[2])		
# 			elif selected == 'staycation':
# 				h = ecr[0].replace('"','')
# 				createStaycations(h, ecr[1], ecr[2], ecr[3], ecr[4])
# 			elif selected == 'booking':
# 				hotel = ecr[2].replace('"', '')
# 				hotel = hotel.strip()
# 				createBookings(ecr[0], ecr[1], hotel)
			
# 	return render_template('upload.html', title=title,)

# # link to upload page
# from dashboard import tc
# app.register_blueprint(tc)

# # already includes the login manager
# from users import *


# if __name__ == "__main__":
# 	app.run(debug=True, port=8000)