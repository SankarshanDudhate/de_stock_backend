from CustomApi import db
from datetime import date, datetime, timedelta


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    phoneNo = db.Column(db.String(10))
    password = db.Column(db.String(50))
    address = db.Column(db.String(100), default='')
    #image = db.Column(db.Text)
    cart = db.Column(db.Integer, default=0)
    type = db.Column(db.String(10), default='buyer')
    wishlist = db.Column(db.JSON)
    enquiredProducts = db.Column(db.JSON)
    adsAvailable = db.Column(db.Integer, default=0)
    company_id = db.Column(db.Integer, default=0)
    contact_person_id = db.Column(db.Integer, default=0)
    firebaseDeviceToken = db.Column(db.String(255), default="fooFX7TBRSuh76m4iIdut6:APA91bFL6RmdyfD1zzTsu5XkS1-aeI3oNdHA4wO-SZCL5Y-fu5YwuNu5h5sbW_HnQ5G0zrxdJvKjdpiPko2krpQ4sMutvXtOtP9LPXiwkQrVAihzWlhoHltPMGE_JGlvFaiXQXyDMDoM")
    shareableKey = db.Column(db.String(1024))

    # products = db.relationship("Product", backref="owner", lazy=True)

    def as_dict(self):
        return {user.name: getattr(self, user.name) for user in self.__table__.columns}

    def __repr__(self):
        return f"({self.__tablename__}: {self.name})\n"


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    details = db.Column(db.String(5000), default='')
    # category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category_id = db.Column(db.Integer)
    subCategory_id = db.Column(db.Integer, default=0)
    #images = db.Column(db.Text(4294000000))
    available = db.Column(db.Boolean, default=True)
    maxQty = db.Column(db.Integer, default=0)
    unit = db.Column(db.String(100),  default='')
    specifications = db.Column(db.JSON, default='')
    latLongs = db.Column(db.JSON, default='')
    address = db.Column(db.String(200),  default='')
    price = db.Column(db.Integer, default=0)
    priceDisclose = db.Column(db.Boolean, default=True)
    views = db.Column(db.Integer, default=0)
    soldCount = db.Column(db.Integer, default=0)
    wishlisted = db.Column(db.Integer, default=0)
    enquiries = db.Column(db.JSON)
    publishedDate = db.Column(db.Date)
    expiryDate = db.Column(db.Date)
    expired = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, nullable=False, default=0)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f"({self.__tablename__}: {self.name})\n"


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    # products = db.relationship("Product", backref="category", lazy=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f"({self.__tablename__}: {self.name})\n"


class SubCategory(db.Model):
    __tablename__ = "sub_category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.Integer)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f"({self.__tablename__}: {self.name})\n"


class Wishlist(db.Model):
    __tablename__ = "wishlist"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    products = db.Column(db.JSON)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f"({self.__tablename__}: {self.user_id})\n"


class Cart(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    # products = db.relationship("Product")
    products = db.Column(db.JSON)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f"({self.__tablename__}: {self.user_id})\n"
		
class PaymentMethods(db.Model):
	__tablename__ = "payment_methods"
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer)
	# products = db.relationship("Product")
	card_number = db.Column(db.String(100))
	card_name = db.Column(db.String(100))
	expiry_date = db.Column(db.Date)
	card_type = db.Column(db.String(100))

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

	def __repr__(self):
		return f"({self.__tablename__}: {self.user_id})\n"
		
class Company(db.Model):
	__tablename__ = "company"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), default='')
	pan_no = db.Column(db.String(10), default='')
	gst_no = db.Column(db.String(20), default='')
	factory_address = db.Column(db.String(200), default='')
	factory_latlong = db.Column(db.JSON)
	office_address = db.Column(db.String(200), default='')
	office_latlong = db.Column(db.JSON)
	what_you_sell = db.Column(db.String(500), default='')
	
	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

	def __repr__(self):
		return f"({self.__tablename__}: {self.user_id})\n"
		
class ContactPerson(db.Model):
	__tablename__ = "contact_person"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(50))
	phone_no = db.Column(db.String(10), default='')
	
	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

	def __repr__(self):
		return f"({self.__tablename__}: {self.user_id})\n"
	
class TempProduct(db.Model):
	__tablename__ = "temp_products"
	id = db.Column(db.Integer, primary_key=True)
	products = db.Column(db.JSON)
	user_id = db.Column(db.Integer)
	order_id = db.Column(db.String(50))

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

	def __repr__(self):
		return f"({self.__tablename__}: {self.user_id})\n"