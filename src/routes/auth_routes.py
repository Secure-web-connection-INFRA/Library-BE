from flask import Blueprint, jsonify, request
from src.controller.auth import AuthService

class AuthBlueprint:
    

    def __init__(self) -> None:
        print("Running")
        pass
    

    def validateAuth():
        print(request.headers)  # Example validation logic
        pass
 
auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.before_request
def validation():
    print("user is running")
    print(request.get_json())


@auth_blueprint.route('/login', methods=['POST'])
def login():
    # AuthBlueprint.validateAuth()
    return "Hello"

@auth_blueprint.route('/signUp', methods=['POST'])
def signUp():
    # Implement signUp logic
    pass

@auth_blueprint.route('/reset', methods=['POST'])
def resetPassword():
    # Implement password reset logic
    pass

