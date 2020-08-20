from CustomApi import db
from datetime import date, datetime, timedelta


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    address = db.Column(db.String(100))
    phoneNo = db.Column(db.String(10))
    products = db.relationship('Product', backref='owner', lazy=True)

    def as_dict(self):
       return {user.name: getattr(self, user.name) for user in self.__table__.columns}

    def __repr__(self):
        return f'({self.__tablename__}: {self.name})\n'



class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    subCategory_id = db.Column(db.Integer)
    # images = db.column(db.JSON)
    available = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


    def __repr__(self):
        return f'({self.__tablename__}: {self.name})\n'



class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return f'({self.__tablename__}: {self.name})\n'



class SubCategory(db.Model):
    __tablename__ = 'sub_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.Integer)

    def __repr__(self):
        return f'({self.__tablename__}: {self.name})\n'
