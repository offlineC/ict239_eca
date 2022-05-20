from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask_login import login_required, current_user
from init import db
from booking_mod import *


tc = Blueprint('trend_chart', __name__)

@tc.route('/trend_chart', methods=['GET'])
def trend_chartpage():
	if request.method == 'GET':
		output = dataOutput()
		
	return render_template('trend_chart.html', title='Package Chart', output = output)
