from flask import Flask, render_template, request
from datetime import datetime, timedelta
# import db setup
from __init__ import *
import pymongo
import csv 

# connect to db to be used globally
client = pymongo.MongoClient('localhost:27017')
db = client.get_database('staycationportal')

"""
note:
pages linked by blueprint are suffixed accordingly 
form pages:
<page>form
eg: 
@def registerform():
listing or normal pages:
<page>page
eg:
@def packagepage():
"""

'''
pages are linked by Blueprint to make the app modular
'''

# link to login/registration page
from auth import login, register
app.register_blueprint(login)
app.register_blueprint(register)

#link to package page
from package import package
app.register_blueprint(package)

# link to individual hotel pages
from hotel import hotel
app.register_blueprint(hotel)

# link to upload page
from upload import upload
app.register_blueprint(upload)

# link to upload page
from trend_chart import tc
app.register_blueprint(tc)

# already includes the login manager
from users import *


if __name__ == "__main__":
	app.run(debug=True,port=8000)