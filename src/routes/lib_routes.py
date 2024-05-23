from flask import Blueprint, jsonify, request

from src.utils.validate import validateJWTToken
from src.utils.customError import CustomException
from src.controller.lib import LibService

lib_blueprint = Blueprint('lib', __name__)

@lib_blueprint.before_request
def validation():
    try:
        validateJWTToken(request.headers.get("Authorization"))
    except CustomException as e:
        return e.message if hasattr(e,"message")  else "Error has occured", 401
    
@lib_blueprint.route('/', methods=['GET'])
def view():
    return LibService.view()

@lib_blueprint.route('/search', methods=['GET'])
def search():
    return LibService.bookId()

@lib_blueprint.route('/download', methods=['POST'])
def download():
    return
