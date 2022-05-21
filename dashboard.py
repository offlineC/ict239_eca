from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from book import *

tc = Blueprint('trend_chart', __name__)

@tc.route('/trend_chart', methods=['GET'])
def trend_chartpage():
	if request.method == 'GET':
		output = getAllBookings()
		checkindates = [ opd.check_in_date for opd in output ]
		totalcosts = [ optc.total_cost for optc in output ]
		hotelnames = [ oph.package.hotel_name for oph in output ]
		totalcostsperdate = [ {'date': str(checkindates[i]), 'finalprice': (checkindates.count(v) * totalcosts[i]), 'hotel': hotelnames[i] } for i,v in enumerate(checkindates) ]
		finaltcpd = [dict(t) for t in {tuple(d.items()) for d in totalcostsperdate}]
		finaltcpd = sorted(finaltcpd, key = lambda n : n['date'])
	return render_template('trend_chart.html', title='Package Chart', output = finaltcpd)