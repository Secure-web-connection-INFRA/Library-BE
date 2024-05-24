from src.db.config import *
from src.db.lib import *
from src.utils.passCrypt import fileEncrypt
import base64

class LibService():

    @staticmethod
    def dto(row):
        image = fileEncrypt(f"src/Books/cover/{row[6]}.jpeg")
        return {
                "id":row[0],
                "title":row[1],
                "description":row[2],
                "author": row[3],
                "publishedOn":row[4],
                "image":image
            }
    
    def view():
        rows = queryDB(libView())
        response = []
        for row in rows:
            response.append(LibService.dto(row))
        
        return response
    
    def bookName(book_name):
        row = queryDB(libViewName(book_name))
        if len(row) != 0:
            book = LibService.dto(row[0])
            # book["url"] = row[0][5]
            return book
        else :
            return f"No book found"
        
    def download(id):
        row = queryDB(libViewId(id))
        if len(row) != 0:
            book = LibService.dto(row[0])
            data, publicKey = fileEncrypt(f"src/Books/{row[0][6]}.pdf",True)
            book["file"] = data
            book["key"] = publicKey
            return book
        else :
            return f"Not available for download"

        