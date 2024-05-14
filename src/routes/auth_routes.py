from flask import Blueprint, jsonify, request
from src.controller.auth import AuthService

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.before_request
def validation():
    print(request.get_json())


@auth_blueprint.route('/login', methods=['POST'])
def login():
    response = request.get_json(silent=True)
    return AuthService.login(response)

@auth_blueprint.route('/signup', methods=['POST'])
def signUp():
    response = request.get_json(silent=True)
    return AuthService.signUp(response)
    
@auth_blueprint.route('/forget-password', methods=['POST'])
def forgetPassword():
    response = request.get_json(silent=True)
    return AuthService.forgetPassword(response)

