from users import User
from staycation import STAYCATION
from app import db

class Booking(db.Document):
	meta = {'collection': 'booking'}
	check_in_date = db.DateTimeField(required=True)
	customer = db.ReferenceField(User)
	package = db.ReferenceField(STAYCATION)
	total_cost = db.FloatField()
	def calculate_total_cost(self):
	self.total_cost = self.package.duration * self.package.unit_cost

	