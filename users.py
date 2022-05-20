from __init__ import *
# from app import db
from flask_login import UserMixin

class User(UserMixin, db.Document):
	# 1) a)
	# Sets up the name of the collection
	meta = {'collection': 'appUsers'}
	# Creates an email field/column in the collection of appUsers with data type as string
	email = db.StringField(max_length=30)
	# Creates a password field/column in the collection of appUsers with data type as string
	password = db.StringField()
	# Creates a name field/column in the collection of appUsers data type as string
	name = db.StringField()

# load user from session
# user object has been passed into the login_user()
@login_manager.user_loader
def loaduser(user_id):
	return User.objects(pk=user_id).first()
