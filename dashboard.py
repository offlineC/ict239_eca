from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from book import *

tc = Blueprint('trend_chart', __name__)

@tc.route('/trend_chart', methods=['GET'])
def trend_chartpage():
	if request.method == 'GET':
		output = dataOutput()
		
	return render_template('trend_chart.html', title='Package Chart', output = output)