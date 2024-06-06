import base64
from src.db.config import *
from src.db.lib import *
from src.utils.passCrypt import fileEncrypt
from src.utils.awsConfig import awsConfig,awsUpload
from src.db.login import findEmailId,getUserRole

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
        try:
            rows = queryDB(libView())
            response = []
#            return [LibService.dto(rows[0]),LibService.dto(rows[1])]
            for row in rows:
                res = LibService.dto(row)
                response.append(res)
            return {"data":response}
        except Exception as e:
            return e
    
    def bookName(book_name):
        try:
            row = queryDB(libViewName(book_name))
            if len(row) != 0:
                book = LibService.dto(row[0])
                return book
            else :
                return f"No book found"
        except Exception as e:
            return "Error has occured" , 500
        
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

    def roleChange(email,role,id): 
        try:
            rows = queryDB(getUserRole(id))
            if rows[0][0].lower() != "admin":
                return "Only Admin user can change the role"
            
            rows = queryDB(findEmailId(email))
            if len(rows):
                queryDB(updateRole(role,email))
                return "Successful changed the role"
            else:
                return "Invalid email address", 500
        except Exception as e:
            return "Unable to process", 500
        
    def uploadBook(data):
        try:
            pdf_base64 = data.get('pdfBase64')
            cover_image_base64 = data.get('coverImageBase64')
            author = data.get('author')
            title = data.get('title')
            desc = data.get("description")
            published_on = data.get('publishedOn')

            # Decode the cover image base64 string
            cover_image_bytes = base64.b64decode(cover_image_base64)
            cover_pdf_bytes = base64.b64decode(pdf_base64)

            # Upload the cover image to S3
            cover_image_key = f"cover/{title.replace(' ', '_')}.jpeg"
            cover_pdf_key = f"{title.replace(' ', '_')}.pdf"

            awsUpload(cover_image_key,cover_image_bytes)
            awsUpload(cover_pdf_key,cover_pdf_bytes,"pdf")
            
            id = f"b00{len(queryDB(libView()))}"
            print(id, title,desc,author,published_on,cover_pdf_key)
            queryDB(insertNewBook(id, title,desc,author,published_on,cover_pdf_key,f"{title.replace(' ', '_')}.jpeg"))
            
            return "Uploaded book successfully"
        except Exception as e:
            return "Something went wrong", 500



