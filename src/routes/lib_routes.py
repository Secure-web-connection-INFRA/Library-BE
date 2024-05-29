from flask import Blueprint, request,abort, jsonify
from flask_cors import cross_origin
import os
from src.utils.validate import validateJWTToken
from src.utils.customError import CustomException
from src.controller.lib import LibService

lib_blueprint = Blueprint('lib', __name__)

def validation():
    try:
        validateJWTToken(request.headers.get("Authorization"))
    except CustomException as e:
        abort(401, e.message if hasattr(e,"message")  else "Error has occured")
    
@lib_blueprint.route('/all', methods=['GET'])
def view():
    validation()
    return jsonify(LibService.view())

@lib_blueprint.route('/search', methods=['GET'])
def search():
    validation()
    book_name = request.args.get('book')
    return LibService.bookName(book_name)

@lib_blueprint.route('/download', methods=['GET'])
def download():
    validation()
    bookId = request.args.get('bookId')
    return LibService.download(bookId)
