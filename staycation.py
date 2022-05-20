from app import db

class STAYCATION(db.Document):
	meta = {'collection': 'staycation'}
	hotel_name = db.StringField(max_length=30)
	duration = db.IntField()
	unit_cost = db.FloatField()
	image_url = db.StringField(max_length=30)
	description = db.StringField(max_length=500)
