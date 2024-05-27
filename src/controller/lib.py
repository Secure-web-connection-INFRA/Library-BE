from src.db.config import *
from src.db.lib import *
from src.utils.passCrypt import fileEncrypt
from src.utils.awsConfig import awsConfig

class LibService():

    @staticmethod
    def dto(row):
        image = awsConfig(f"cover/{row[6]}")
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
            return book
        else :
            return f"No book found"
        
    def download(id):
        row = queryDB(libViewId(id))
        try:
            if len(row) != 0:
                book = LibService.dto(row[0])

                base64_data = awsConfig(row[0][5])
                if type(base64_data).__name__ == "str":
                    data, publicKey = fileEncrypt(base64_data)
                    book["file"] = data
                    book["key"] = publicKey
                    return book
                else:
                    raise "Unable to access"
            else :
                return f"Not available for download", 503
        except Exception as e:
            return "No download option", 503

        