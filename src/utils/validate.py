import re
import uuid
from datetime import datetime, timedelta

def validateEmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generateResetToken():
    new_time = datetime.now() + timedelta(hours=2)
    token = str(uuid.uuid4())
    return "/".join(["127.0.0.1:5000/reset",token ]), str(token)