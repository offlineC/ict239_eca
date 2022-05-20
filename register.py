from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from forms import *
from users import *

register = Blueprint('register',__name__)

@register.route('/register', methods=['POST','GET'])
def registerform():
	title='Register'
	errmessage = ''
	scmessage = ''
	form = registerf()
	# if user is already logged in, redirect them to the packages page
	if current_user.is_authenticated:
		return redirect(url_for('package.packagepage'))
		
	if request.method == 'POST':
		if form.validate():
			is_existingUser = User.objects(email=form.email.data).first()
			if is_existingUser is None:
				email = form.email.data
				password = form.password.data
				name = form.name.data
				user = User(email=email, password=password, name=name).save()
				scmessage='Registration successful!'
			else:
				errmessage='User already exists'
				
		
	return render_template('register.html', title=title, form=form, errmessage=errmessage, scmessage=scmessage)

