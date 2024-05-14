import sqlite3

dbName = "myDB.db"

def queryDB(query = None):
    try:
        with sqlite3.connect(dbName) as conn:
            cur = conn.cursor()
            if query != None:
                cur.execute(query) 
                row = cur.fetchall()
                return row
            else:
                return None
    except sqlite3.Error as e:
        print(e)
        raise f"SQL Error in query {query}"