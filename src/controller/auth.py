import random
from src.utils.validate import validateEmail
from src.utils.customError import CustomException
from src.utils.passCrypt import validate_password,hash_password
from src.db.login import *
from src.db.config import *

class AuthService():
    
    def validateAuth():
        """Abstract method to validate authentication."""
        pass
       
    def login():
        """Abstract method to handle login."""
        pass
   
    def signUp(response: dict):
        try:
            (name, email, password) = response.values()
            if not validateEmail(email):
                raise CustomException("invalid email")
            elif bool(queryDB(findEmailId(email))[0][0]):
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
   
    def resetPassword():
        """Abstract method to handle password reset."""
        pass
