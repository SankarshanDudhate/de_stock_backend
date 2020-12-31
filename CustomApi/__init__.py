# Imports
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder

# Database
db = SQLAlchemy()
seeder = FlaskSeeder()

from CustomApi.models import *


def create_app():
    # instantiate the app
    app = Flask(__name__)
	#static_url_path='/static', static_folder='/static'
    app.config.from_object('CustomApi.config.BaseConfig')

    db.init_app(app)
    seeder.init_app(app, db)

    # enable CORS for unrestrected js request

    from CustomApi.main.routes import main
    from CustomApi.products.routes import api as products
    from CustomApi.users.routes import api as users
    from CustomApi.cart.routes import api as cart
    from CustomApi.login.routes import api as login
    from CustomApi.otp.routes import api as otp
    from CustomApi.signup.routes import api as signup
    from CustomApi.wishlist.routes import api as wishlist
    from CustomApi.images.routes import api as images
    from CustomApi.payments.routes import api as payments

    app.register_blueprint(main)
    app.register_blueprint(products, url_prefix='/products')
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(cart, url_prefix='/cart')
    app.register_blueprint(login, url_prefix='/login')
    app.register_blueprint(otp, url_prefix='/otp')
    app.register_blueprint(signup, url_prefix='/signup')
    app.register_blueprint(wishlist, url_prefix='/wishlist')
    app.register_blueprint(images, url_prefix='/images')
    app.register_blueprint(payments, url_prefix='/payments')

    return app
