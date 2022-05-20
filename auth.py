from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from forms import *
from users import User

auth = Blueprint('auth',__name__)

auth.route('/')
auth.route('/login', methods=['POST','GET'])
def login():
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

auth.route('/logout', methods=['GET'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('auth.login'))



auth.route('/register', methods=['POST','GET'])
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

