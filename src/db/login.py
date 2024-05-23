def insertUser(id,name,email,password):
    return f"INSERT INTO auth (id,emailAddress,name,password)VALUES ('{id}','{email}','{name}','{password}');"

def fetchAllId():
    return f"SELECT id FROM auth;"

def findEmailId(email):
    return f"SELECT id, password, name FROM auth WHERE emailAddress='{email}';"

def forgetPass(token,id):
    return f"INSERT INTO authReset (token, id) VALUES ('{token}','{id}');"

def findTokenId(token):
    return f"SELECT id, strftime('%s', 'now') - strftime('%s', createdAt) < 7200 FROM authReset WHERE token='{token}'"

def deleteToken(token):
    return f"DELETE FROM authReset WHERE token = '{token}';"

def updatePassword(id, password):
    return f"UPDATE auth SET password ='{password}' WHERE id ={id};"

def insertOtp(email,otp):
    return f"INSERT INTO otp ('emailAddress', 'otp') VALUES ('{email}', {otp});"

def findEmailOTP(email):
    return f"SELECT otp from otp WHERE emailAddress='{email}';"

def findEmailOtp(email):
    return f"SELECT otp from otp WHERE emailAddress='{email}' AND (attempt < 4 OR attempt IS NULL) AND (julianday('now') - julianday(createdAt)) * 24 * 60 <= 120;"

def delEmailOtp(email):
    return f"DELETE FROM otp WHERE emailAddress = '{email}';"

def updateEmailOtp(email):
    return f"UPDATE otp SET attempt = attempt + 1 WHERE emailAddress = {email};"