import mysql.connector

from src.config import DBConfig
from src.utils.customError import CustomException

db_config = {
    'user': DBConfig.DB_USER,
    'password': DBConfig.DB_PASS,
    'host': DBConfig.DB_HOST,  # RDS endpoint
    'database': DBConfig.DB_NAME,
    'raise_on_warnings': True
}

def queryDB(query = None):
    try:
        with mysql.connector.connect(**db_config) as conn:
            cur = conn.cursor()
            if query != None:
                print(query)
                cur.execute(query) 
                row = cur.fetchall()
                cur.close()
                conn.close()
                return row
            else:
                return None
    except Exception as e:
        raise CustomException(f"SQL Error in query {query} \n {e}")