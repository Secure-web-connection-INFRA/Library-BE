def insertUser(id, name, email, password):
    query = "INSERT INTO auth (id, emailAddress, name, password) VALUES (?, ?, ?, ?);"
    return query, (id, email, name, password)

def fetchAllId():
    query = "SELECT id FROM auth;"
    return query, ()

def findEmailId(email):
    query = "SELECT id, password, name, role FROM auth WHERE emailAddress = ?;"
    return query, (email,)

def forgetPass(token, id):
    query = "INSERT INTO authReset (token, id) VALUES (?, ?);"
    return query, (token, id)

def findTokenId(token):
    query = "SELECT id, strftime('%s', 'now') - strftime('%s', createdAt) < 7200 FROM authReset WHERE token = ?;"
    return query, (token,)

def deleteToken(token):
    query = "DELETE FROM authReset WHERE token = ?;"
    return query, (token,)

def updatePassword(id, password):
    query = "UPDATE auth SET password = ? WHERE id = ?;"
    return query, (password, id)

def insertOtp(email, otp):
    query = "INSERT INTO otp (emailAddress, otp) VALUES (?, ?);"
    return query, (email, otp)

def findEmailOTP(email):
    query = "SELECT otp FROM otp WHERE emailAddress = ?;"
    return query, (email,)

def findEmailOtp(email):
    query = "SELECT otp FROM otp WHERE emailAddress = ? AND (attempt < 4 OR attempt IS NULL) AND (julianday('now') - julianday(createdAt)) * 24 * 60 <= 120;"
    return query, (email,)

def delEmailOtp(email):
    query = "DELETE FROM otp WHERE emailAddress = ?;"
    return query, (email,)

def getUserRole(id):
    query = "SELECT role FROM auth WHERE id=?;"
    return query, (id,)

def updateEmailOtp(email):
    query = "UPDATE otp SET attempt = attempt + 1 WHERE emailAddress = ?;"
    return query, (email,)