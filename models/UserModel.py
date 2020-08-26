from db import db
from hashlib import sha256
from random import randint

class UserModel(db.Model):
	__tablename__ = 'Users'

	user_id = db.Column(db.Integer(), primary_key = True)
	first_name = db.Column(db.String(20))
	last_name = db.Column(db.String(20))
	email = db.Column(db.String(50), unique = True)
	password = db.Column(db.String(80))
	user_type = db.Column(db.String(10))
	picture = db.Column(db.String(100))
	active_state = db.Column(db.Boolean())
	recovery_key = db.Column(db.String(64))

	customers = db.relationship('OrderModel', backref = 'customer', cascade = 'all, delete-orphan', lazy = 'dynamic', foreign_keys = 'OrderModel.customer_id')
	favourites = db.relationship('FavouriteModel', backref = 'user', cascade = 'all, delete-orphan', lazy = 'dynamic')
	products = db.relationship('ProductModel', backref = 'user', cascade = 'all, delete-orphan', lazy = 'dynamic')
	reports = db.relationship('ReportModel', backref = 'user', cascade = 'all, delete-orphan', lazy = 'dynamic')
	vendors = db.relationship('OrderModel', backref = 'vendor', cascade = 'all, delete-orphan', lazy = 'dynamic', foreign_keys = 'OrderModel.vendor_id')

	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.user_type = 'Normal'
		self.picture = 'default'
		self.active_state = True
		self.recovery_key = sha256(str(randint(1, 9999)).encode('utf-8')).hexdigest()
	
	@classmethod
	def find_by_id(cls, user_id):
		return cls.query.filter_by(user_id = user_id).first()
	
	@classmethod
	def find_by_email(cls, email):
		return cls.query.filter_by(email = email).first()
	
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
	
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
