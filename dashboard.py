from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from book import *

tc = Blueprint('trend_chart', __name__)

@tc.route('/trend_chart', methods=['GET'])
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
		# checkindates = [ opd.check_in_date for opd in output ]
		# totalcosts = [ optc.total_cost for optc in output ]
		# hotelnames = [ oph.package.hotel_name for oph in output ]
		totalcostsperdate = [ {'date': str(v['check_in_date']), 'finalprice': (countOcc(v['package']['hotel_name'], v['check_in_date']) * v['total_cost']) , 'hotel': v['package']['hotel_name'] } for i,v in enumerate(output) ]
		finaltcpd = [dict(t) for t in {tuple(d.items()) for d in totalcostsperdate}]
		finaltcpd = sorted(finaltcpd, key = lambda n : n['date'])
		print(finaltcpd)
	return render_template('trend_chart.html', title='Package Chart', output = finaltcpd)