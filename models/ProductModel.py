from db import db

class ProductModel(db.Model):
	__tablename__ = 'Products'

	product_id = db.Column(db.Integer(), primary_key = True)
	user_id = db.Column(db.Integer(), db.ForeignKey('Users.user_id', ondelete = 'CASCADE'))
	category_id = db.Column(db.Integer(), db.ForeignKey('Categories.category_id', ondelete = 'CASCADE'))
	name = db.Column(db.String(20))
	description = db.Column(db.String(255))
	price = db.Column(db.Float(precision = 2))
	image = db.Column(db.String(100))
	visible = db.Column(db.Boolean())

	favourites = db.relationship('FavouriteModel', backref = 'product', cascade = 'all, delete-orphan', lazy = 'dynamic')
	orders = db.relationship('OrderModel', backref = 'product', cascade = 'all, delete-orphan', lazy = 'dynamic')
	opinions = db.relationship('OpinionModel', backref = 'product', cascade = 'all, delete-orphan', lazy = 'dynamic')

	def __init__(self, user_id, category_id, name, description, price, image):
		self.user_id = user_id
		self.category_id = category_id
		self.name = name
		self.description = description
		self.price = price
		self.image = image
		self.visible = True

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
	
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()