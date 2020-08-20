from flask import Blueprint, redirect, render_template
from CustomApi.models import *

main = Blueprint('main', __name__)


@main.route('/')
def index():
    db.create_all()
    return "This is the Home Page"
    # return render_template('index.html')