from flask import Blueprint, jsonify, request
from CustomApi.models import *

api = Blueprint("wishlist", __name__)

