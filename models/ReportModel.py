from db import db

class ReportModel(db.Model):
	__tablename__ = 'Reports'

	report_id = db.Column(db.Integer(), primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete = 'CASCADE'))
	comment = db.Column(db.String(150))

	def __init__(self, user_id, comment):
		self.user_id = user_id
		self.comment = comment
	
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
	
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()