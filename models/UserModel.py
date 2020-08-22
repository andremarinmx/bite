from db import db

class UserModel(db.Model):
	__tablename__ = 'Users'

	user_id = db.Column(db.Integer(), primary_key = True)
	first_name = db.Column(db.String(20))
	last_name = db.Column(db.String(20))
	email = db.Column(db.String(50), unique = True)
	password = db.Column(db.String(80))

	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
	
	def json(self):
		return {
			"user_id": self.user_id,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"email": self.email
		}

	@classmethod
	def find_by_id(cls, user_id):
		return cls.query.filter_by(user_id = user_id).first()
	
	@classmethod
	def find_by_email(cls, email):
		return cls.query.filter_by(email = email).first()
	
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
