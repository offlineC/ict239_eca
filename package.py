from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask_login import login_required
from init import db
from hotel_mod import *

package = Blueprint('package',__name__)

@package.route('/package', methods=['GET'])
# set page to be accessble after login only
@login_required
def packagepage():
	if request.method == 'GET':
		hotels = getAllHotels()
	return render_template('package.html', title='Package', hotels=hotels)

