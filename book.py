from users import User
from staycation import STAYCATION
from app import db

class Booking(db.Document):
	# 1) a)
	# Sets up the name of the collection
	meta = {'collection': 'booking'}
	# Creates a check in date field/column in the collection of book as data type datetime
	check_in_date = db.DateTimeField(required=True)
	# Creates a customer field/column in the collection of book that REFERENCES the user collection
	customer = db.ReferenceField(User)
	# Creates a package field/column in the collection of book that REFERENCES the staycation collection
	package = db.ReferenceField(STAYCATION)
	# Creates a total cost field/column in the collection of book as data type float
	total_cost = db.FloatField()

	# Calculates the total cost of each package with its own unit_cost multiplied by its own duration. When this method is called, it just returns the value of the total cost.
	def calculate_total_cost(self):
		self.total_cost = self.package.duration * self.package.unit_cost

