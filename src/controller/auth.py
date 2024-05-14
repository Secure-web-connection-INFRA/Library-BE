import random
from src.utils.validate import validateEmail, generateResetToken
from src.utils.customError import CustomException
from src.utils.email import email as emailSender
from src.utils.templates import reset_email_template
from src.utils.passCrypt import validate_password,hash_password
from src.db.login import *
from src.db.config import *

class AuthService():
    def login(response: dict):
        try:
            (email, password) = response.values()

            row = queryDB(findEmailId(email))
            if not len(row):
                raise CustomException("Emailaddress does not exist")
            
            if validate_password(password,row[0][1]):
                return "JWT"
            else:
                return "Invalid password", 401
            
        except CustomException as e:
            return e.message if hasattr(e,"message")  else "Error has occured", 401
            
    def signUp(response: dict):
        try:
            (name, email, password) = response.values()
            if not validateEmail(email):
                raise CustomException("invalid email")
            elif len(queryDB(findEmailId(email))):
                raise CustomException("Emailaddress already exist")
            
            rows = queryDB(fetchAllId())
            id = 0

            while True:
                id = random.randint(100000, 999999)
                if not id in rows:
                    break
            
            hashedPass = hash_password(password)
            
            queryDB(insertUser(id, name, email, hashedPass))

            return "User has been successfully created"
        except CustomException as e:
            return e.message if hasattr(e,"message")  else "Error has occured"
   
    def forgetPassword(response: dict):
        try:
            email = response["email"]

            if not validateEmail(email):
                raise CustomException("invalid email")
            elif len(queryDB(findEmailId(email))) == 0:
                raise CustomException("Emailaddress not exist")
            
            reseturl, token = generateResetToken()

            # store the token
            queryDB(resetAuth(token,email))

            emailSender.sendEmail(reset_email_template,email,reseturl)          
            
            return "Reset link is successfully sent"
        except CustomException as e:
            return e.message if hasattr(e,"message")  else "Error has occured"
   
