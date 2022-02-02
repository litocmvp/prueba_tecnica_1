from flask import Blueprint

private_bp = Blueprint('private', __name__)

from . import private_mexico, private_user