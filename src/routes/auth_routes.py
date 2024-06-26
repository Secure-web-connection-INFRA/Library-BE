from flask import Blueprint, request
from src.controller.auth import AuthService

from src.utils.email import Email
from src.utils.templates import reset_email_template
auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/test', methods=['GET'])
def test():
    Email.sendEmail(reset_email_template,"aswinrockz10@gmail.com",reset_url="reseturl")  
    return "Working fine"

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

@auth_blueprint.route('/otp', methods=['POST'])
def otp():
    # 4 attempt and 2hrs time duration
    json = request.get_json(silent=True)
    return AuthService.otp(json)
