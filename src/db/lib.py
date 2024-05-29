def libView():
    query = "SELECT * FROM booklist;"
    return query, ()

def libViewName(book_name):
    query = "SELECT * FROM booklist WHERE BTitle LIKE ?;"
    return query, (f'%{book_name}%',)

def libViewId(id):
    query = "SELECT * FROM booklist WHERE bID LIKE ?;"
    return query, (f'%{id}%',)