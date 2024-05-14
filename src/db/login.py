def insertUser(id,name,email,password):
    return f"INSERT INTO auth (id,emailAddress,name,password)VALUES ('{id}','{email}','{name}','{password}');"

def fetchAllId():
    return f"SELECT id FROM auth;"

def findEmailId(email):
    return f"SELECT id, password, name FROM auth WHERE emailAddress='{email}';"

def forgetPass(token,id):
    return f"INSERT INTO authReset (token, id)VALUES ('{token}','{id}');"

def findTokenId(token):
    return f"SELECT id, strftime('%s', 'now') - strftime('%s', createdAt) < 7200 FROM authReset WHERE token={token}"

def deleteToken(token):
    return f"DELETE FROM authReset WHERE token = '{token}';"

def updatePassword(id, password):
    return f"UPDATE auth SET password ='{password}' WHERE id ={id};"