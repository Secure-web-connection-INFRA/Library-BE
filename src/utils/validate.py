import re
import uuid
import jwt
from datetime import datetime

from src.config import Config
from src.utils.customError import CustomException

def validateEmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generateResetToken():
    token = str(uuid.uuid4())
    return "/".join([f"{Config.BASEURL}/reset",token ]), str(token)

def generateJWTToken(payload):
    secret_key = Config.JWT_SECRET
    # Generate the JWT token
    return jwt.encode(payload, secret_key, algorithm='HS256')

def validateJWTToken(jwtToken):
    try:
        jwtToken=jwtToken.replace("Bearer ", '')
        decoded_payload = jwt.decode(jwtToken, Config.JWT_SECRET, algorithms=['HS256'])
        expiration_time = datetime.utcfromtimestamp(decoded_payload['exp'])
        current_time = datetime.utcnow()  

        if current_time > expiration_time:
            raise CustomException("Token has expired")
        else:
            return decoded_payload
        
    except jwt.ExpiredSignatureError:
        raise CustomException("Token has expired")
    except jwt.InvalidTokenError:
        raise CustomException("Invalid token")
    except CustomException as e:
        raise e