def libView():
    return "SELECT * FROM booklist"

def libView(id):
    return f"SELECT * FROM booklist WHERE bid = {id}"