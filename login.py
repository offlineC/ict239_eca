from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from forms import *
from users import *

login = Blueprint('login',__name__)

@login.route('/login', methods=['POST','GET'])
@login.route('/')
def loginform():
	title='Login'
	errmessage = ''
	form = loginf()
	# if user is already logged in, redirect them to the packages page
	if current_user.is_authenticated:
		return redirect(url_for('package.packagepage'))

	if request.method == 'POST':
		errmessage = 'did not submit data'
		if form.validate():
			errmessage == ''
			is_existingUser = User.objects(email=form.email.data).first()
			if is_existingUser:
				# no hashing added to password, direct password comparison
				# errmessage = str(dir(is_existingUser))
				if(is_existingUser.password == form.password.data):
					login_user(is_existingUser)
					return redirect(url_for('package.packagepage'))
				else:
					errmessage = 'Wrong password'
				pass
			else:
				errmessage='User account does not exist'
	return render_template('login.html', title=title, form=form, errmessage=errmessage)

@login.route('/logout', methods=['GET'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('login.loginform'))

