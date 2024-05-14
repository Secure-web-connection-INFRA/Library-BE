import hashlib
import uuid

def passwordCipher(password):
    lenth = len(password)
    shift = round(lenth / 5) * 3
    extend = "^*2351*(^<?!/+_-&@%|{'~`,."
    encrypt = []
    newPass = password + extend
    for idx in range(0,lenth):
        newidx = idx + shift
        
        if len(newPass) > newidx:
            newidx = len(newPass) - newidx 
        encrypt.append(newPass[newidx])

    return ''.join(encrypt)

def hash_password(password):
    password = passwordCipher(password)
    print(":: cipher",password)
    hashed_password = hashlib.sha512((password).encode()).hexdigest()
    return hashed_password

def validate_password(password, hashed_password):
    new_hashed_password = hash_password(password)
    return new_hashed_password == hashed_password