import hashlib
from src.config import Config
import base64
import hmac

def passwordCipher(password):
    lenth = len(password)
    shift = round(lenth / 5) * 3
    extend = Config.CIPHER_EXTEND
    encrypt = []
    newPass = password + extend
    for idx in range(0,lenth):
        newidx = idx + shift
        
        if len(newPass) > newidx:
            newidx = len(newPass) - newidx 
        encrypt.append(newPass[newidx])

    return ''.join(encrypt)

def hash_password(password):
#    password = passwordCipher(password)
    
    hashed_password = hashlib.sha512((password).encode()).hexdigest()
    return hashed_password

def validate_password(password, hashed_password):
    new_hashed_password = hash_password(password)
    return new_hashed_password == hashed_password

def generate_hmac(data):
    hmac_digest = hmac.new(Config.FILE_CRYPT.encode(), data.encode(), hashlib.sha256).hexdigest()
    return hmac_digest

def fileEncrypt(path,ishamc = False):
    with open(path, "rb") as image_file:
        image_data = image_file.read()
        base64_encoded_data = base64.b64encode(image_data).decode("utf-8")

    if ishamc:
        return base64_encoded_data, generate_hmac(base64_encoded_data)
    else:
        return base64_encoded_data
