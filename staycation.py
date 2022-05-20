from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app import db

class STAYCATION(db.Document):
	# 1) a)
	# Sets up the name of the collection
	meta = {'collection': 'staycation'}
	# Creates a hotel name field/column in the collection of staycation with data type as string
	hotel_name = db.StringField(max_length=30)
	# Creates a duration field/column in the collection of staycation with data type as integer
	duration = db.IntField()
	# Creates a unit cost field/column in the collection of staycation with data type as float
	unit_cost = db.FloatField()
	# Creates an image url field/column in the collection of staycation with data type as string
	image_url = db.StringField(max_length=30)
	# Creates a description field/column in the collection of staycation with data type as string
	description = db.StringField(max_length=500)

def getAllHotels():
	hotels = STAYCATION.objects()
	return hotels

def getHotelById(id):
	hotel = STAYCATION.objects(id=id).first()
	return hotel

def getHotelDataById(id):
	hotel = STAYCATION.objects(id=id).first()
	return hotel._data

def getHotelByHotelName(hname):
	hotel = STAYCATION.objects()
	for h in hotel:
		if h['hotel_name'] == hname:
			return h

package = Blueprint('package',__name__)

@package.route('/package', methods=['GET'])
# set page to be accessble after login only
@login_required
def packagepage():
	if request.method == 'GET':
		hotels = getAllHotels()
	return render_template('package.html', title='Package', hotels=hotels)
