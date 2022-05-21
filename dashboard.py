from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from book import *
from users import *

tc = Blueprint('trend_chart', __name__)

def removeDupeDic(thisdictionary):
	return [dict(t) for t in {tuple(d.items()) for d in thisdictionary}]
@tc.route('/trend_chart', methods=['GET'])
# set page to be accessble after login only
@login_required
def trend_chartpage():
	def countOcc(hotelname, date):
		op = getAllBookings()
		num = 0
		for i,n in enumerate(op):
			if n['check_in_date'] == date and n['package']['hotel_name'] == hotelname:
				num += 1
		return num
	
	if request.method == 'GET':
		output = getAllBookings()
		totalcostsperdate = [ {'date': str(v['check_in_date']), 'finalprice': (countOcc(v['package']['hotel_name'], v['check_in_date']) * v['total_cost']) , 'hotel': v['package']['hotel_name'] } for i,v in enumerate(output) ]
		finaltcpd = removeDupeDic(totalcostsperdate)
		finaltcpd = sorted(finaltcpd, key = lambda n : n['date'])
	return render_template('trend_chart.html', title='Dashboard', output = finaltcpd, isDashboard=True, tablename='Total Income')

@tc.route('/trend_chart/due_per_user/', methods=['GET'])
# set page to be accessble after login only
@login_required
def dueperuser():
	return render_template('trend_chart.html', title='Dashboard', output = None, isDashboard=True, tablename='Due Per User', users=getAllUsers())

@tc.route('/trend_chart/due_per_user/<id>', methods=['GET'])
# set page to be accessble after login only
@login_required
def dueperuserload(id:str):
	def calTotal(hotelname,arr):
		getCost = [ b for b in arr if b['package']['hotel_name'] == hotelname]
		return len(getCost)

	thisuser = getUserById(id)
	output = getAllBookings()
	userBookings = [ a for a in output if a['customer']['name'] == thisuser['name']]
	outputBooking = [{'hotel':v['package']['hotel_name'], 'count':calTotal(v['package']['hotel_name'], userBookings)} for i,v in enumerate(userBookings)]
	outputBooking = removeDupeDic(outputBooking)
	return render_template('trend_chart.html', title='Dashboard', output = outputBooking, isDashboard=True, tablename='Due Per User', users=getAllUsers(), thisuser=thisuser)

@tc.route('/trend_chart/due_per_hotel', methods=['GET'])
# set page to be accessble after login only
@login_required
def dueperhotel():
	
	return render_template('trend_chart.html', title='Dashboard', output = None, isDashboard=True, tablename='Due Per Hotel',hotels=getAllHotels())

@tc.route('/trend_chart/due_per_hotel/<id>', methods=['GET'])
# set page to be accessble after login only
@login_required
def dueperhotelload(id:str):
	def calTotal(custName,arr):
		getCost = [ b for b in arr if b['customer']['name'] == custName]
		return len(getCost)

	thishotel = getHotelById(id)
	output = getAllBookings()
	userBookings = [ a for a in output if a['package']['hotel_name'] == thishotel['hotel_name']]
	outputBooking = [{'customername':v['customer']['name'], 'count':calTotal(v['customer']['name'], userBookings)} for i,v in enumerate(userBookings)]
	outputBooking = removeDupeDic(outputBooking)
	print(outputBooking)
	return render_template('trend_chart.html', title='Dashboard', output = outputBooking, isDashboard=True, tablename='Due Per Hotel',hotels=getAllHotels(), thishotel=thishotel)