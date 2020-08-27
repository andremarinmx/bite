from db import db

class OpinionModel(db.Model):
	__tablename__ = 'Opinions'

	opinion_id = db.Column(db.Integer(), primary_key = True)
	product_id = db.Column(db.Integer(), db.ForeignKey('Products.product_id', ondelete = 'CASCADE'))
	rating = db.Column(db.Integer())
	comment = db.Column(db.String(50))

	def __init__(self, product_id, rating, comment):
		self.product_id = product_id
		self.rating = rating
		self.comment = comment

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
	
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()