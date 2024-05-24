def libView():
    return "SELECT * FROM booklist;"

def libViewName(book_name):
    return f"SELECT * FROM booklist WHERE BTitle like '{book_name}'"

def libViewId(id):
    return f"SELECT * FROM booklist WHERE bID like '{id}'"
