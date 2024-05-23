from src.db.config import *
from src.db.lib import *

class LibService():

    @staticmethod
    def dto(row):
        return {
                "id":row[0],
                "title":row[1],
                "description":row[2],
                "author": row[3],
                "publishedOn":row[4],
                "image":row[6] # how to get the image
            }
    
    def view():
        rows = queryDB(libView)
        response = []
        for row in rows:
            response.append(LibService.dto(row))
        
        return response
    
    def bookId(id):
        row = queryDB(libView)
        book = LibService.dto(row)
        book["url"] = row[5]
        return book

        