from flask import Flask
from flask_mongoengine import MongoEngine, Document
from flask_login import LoginManager
import pymongo

def create_app():
	app = Flask(__name__)

	# 1) a)
	# Set up and connects the database to the app
	app.config['MONGODB_SETTINGS'] = {
		'db':'eca',
		'host':'localhost'
	}

	# set upload folder for csv files
	app.config['UPLOAD_FOLDER'] = 'assets/files'

	app.static_folder = 'assets'
	# Set db as the reference the established database connection
	db = MongoEngine(app)
	app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
	login_manager = LoginManager()
	login_manager.init_app(app)
	# correction to routing, needs to reference auth.login as endpoint when user is not logged in
	login_manager.login_view = 'auth.login'
	
	return app, db, login_manager

app, db, login_manager = create_app()