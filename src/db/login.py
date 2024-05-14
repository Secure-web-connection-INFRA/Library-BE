def insertUser(id,name,email,password):
    return f"INSERT INTO auth (id,emailAddress,name,password)VALUES ('{id}','{email}','{name}','{password}');"

def fetchAllId():
    return f"SELECT id FROM auth;"

def findEmailId(email):
    return f"SELECT emailAddress, password FROM auth WHERE emailAddress='{email}';"

def resetAuth(token,email):
    return f"INSERT INTO authReset (token, email)VALUES ('{token}','{email}');"