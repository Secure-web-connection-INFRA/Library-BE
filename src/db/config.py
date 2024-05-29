import sqlite3

from src.utils.customError import CustomException
from src.config import Config

def queryDB(queryParam):
    try:
        (query,param)=queryParam
        with sqlite3.connect(Config.DATABASE_NAME) as conn:
            cur = conn.cursor()
            if query != None:
                print(query)
                cur.execute(query,param) 
                row = cur.fetchall()
                return row
            else:
                return None
    except sqlite3.Error as e:
        raise CustomException(f"SQL Error in query {query} \n {e}")
