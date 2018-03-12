from flask import Blueprint
from flask_restplus import Api

from .users import api as user_ns

blueprint = Blueprint('api', __name__, url_prefix='/v1')
api = Api(blueprint, version='1.0')

api.add_namespace(user_ns)
