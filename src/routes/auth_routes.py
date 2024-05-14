from flask import Blueprint, request
from src.controller.auth import AuthService

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.before_request
def validation():
    print(request.get_json())


@auth_blueprint.route('/login', methods=['POST'])
def login():
    json = request.get_json(silent=True)
    return AuthService.login(json)

@auth_blueprint.route('/signup', methods=['POST'])
def signUp():
    json = request.get_json(silent=True)
    return AuthService.signUp(json)
    
@auth_blueprint.route('/forget-password', methods=['POST'])
def forgetPassword():
    json = request.get_json(silent=True)
    return AuthService.forgetPassword(json)

@auth_blueprint.route('/reset', methods=['PUT'])
def resetPassword():
    json = request.get_json(silent=True)
    return AuthService.resetPassword(json)
