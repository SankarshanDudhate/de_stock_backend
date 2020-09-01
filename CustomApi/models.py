from CustomApi import db
from datetime import date, datetime, timedelta


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    phoneNo = db.Column(db.String(10))
    password = db.Column(db.String(50))
    address = db.Column(db.String(100))
    cart = db.Column(db.Integer)
    type = db.Column(db.String(10))
    wishlist = db.Column(db.Integer)
    adsAvailable = db.Column(db.Integer)

    # products = db.relationship("Product", backref="owner", lazy=True)

    def as_dict(self):
        return {user.name: getattr(self, user.name) for user in self.__table__.columns}

    def __repr__(self):
        return f"({self.__tablename__}: {self.name})\n"


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    details = db.Column(db.String(100))
    # category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category_id = db.Column(db.Integer)
    subCategory_id = db.Column(db.Integer)
    images = db.column(db.Text)
    available = db.Column(db.Boolean)
    minQty = db.Column(db.Integer)
    unit = db.Column(db.String(100))
    specifications = db.Column(db.String(100))
    location = db.Column(db.String(100))
    price = db.Column(db.Integer)
    priceDisclose = db.Column(db.Integer)
    views = db.Column(db.Integer)
    soldCount = db.Column(db.Integer)

    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

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
    product_ids = db.Column(db.Text)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f"({self.__tablename__}: {self.user_id})\n"
