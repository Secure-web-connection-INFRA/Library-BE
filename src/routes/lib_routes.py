from flask import Blueprint, jsonify, request

lib_blueprint = Blueprint('lib', __name__)

@lib_blueprint.route('/search', methods=['POST'])
def search():
    # Implement login logic
    print("works")
    return "sd"

@lib_blueprint.route('/download', methods=['POST'])
def download():
    return
