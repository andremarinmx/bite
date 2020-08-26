from db import db

class FavouriteModel(db.Model):
	__tablename__ = 'Favourites'

	favourite_id = db.Column(db.Integer(), primary_key = True)
	user_id = db.Column(db.Integer(), db.ForeignKey('Users.user_id', ondelete = 'CASCADE'))
	product_id = db.Column(db.Integer(), db.ForeignKey('Products.product_id', ondelete = 'CASCADE'))

	def __init__(self, user_id, product_id):
		self.user_id = user_id
		self.product_id = product_id

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
	
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()