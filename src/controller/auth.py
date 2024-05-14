import random
from src.utils.validate import validateEmail, generateResetToken
from src.utils.customError import CustomException
from src.utils.email import email as emailSender
from src.utils.templates import reset_email_template
from src.utils.passCrypt import validate_password,hash_password
from src.db.login import *
from src.db.config import *

class AuthService():
    def login(request: dict):
        try:
            (email, password) = request.values()

            row = queryDB(findEmailId(email))
            if not len(row):
                raise CustomException("Emailaddress does not exist")
            
            if validate_password(password,row[0][1]):
                return "JWT"
            else:
                return "Invalid password", 401
            
        except CustomException as e:
            return e.message if hasattr(e,"message")  else "Error has occured", 401
            
    def signUp(request: dict):
        try:
            (name, email, password) = request.values()
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
   
    def forgetPassword(request: dict):
        try:
            email = request["email"]

            rows = queryDB(findEmailId(email))
            if len(rows) == 0:
                raise CustomException("Emailaddress not exist")
            
            reseturl, token = generateResetToken()
            
            # store the token
            queryDB(forgetPass(token,rows[0][0]))

            emailSender.sendEmail(reset_email_template,email,reseturl)          
            
            return "Reset link is successfully sent"
        except CustomException as e:
            return e.message if hasattr(e,"message")  else "Error has occured"
   
    def resetPassword(request:dict):
        try:
            (token, password) = request

            hashValue = hash_password(password)

            rows = queryDB(findTokenId(token))

            print(rows,"rows ::")
            if len(rows) == 0:
                raise CustomException("Invalid token")
            elif rows[0][1] == 0:
                raise CustomException("Token expired. Try again")
            else:
                queryDB(deleteToken(token))
                queryDB(updatePassword(rows[0][0],hashValue))
            
            return "Password has been updated. Try login"
        except CustomException as e:
            return e.message if hasattr(e,"message")  else "Error has occured"
   

