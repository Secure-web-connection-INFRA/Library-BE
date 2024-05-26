import sqlite3
import logging
from src.utils.customError import CustomException
from src.config import Config

def queryDB(query = None):
    try:
        with sqlite3.connect("library.db") as conn:
            cur = conn.cursor()
            if query != None:
                logging.info(query)
                cur.execute(query) 
                row = cur.fetchall()
                return row
            else:
                return None
    except sqlite3.Error as e:
        raise CustomException(f"SQL Error in query {query} \n {e}")
