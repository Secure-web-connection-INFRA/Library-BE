def libView():
    query = "SELECT * FROM booklist;"
    return query, ()

def libViewName(book_name):
    query = "SELECT * FROM booklist WHERE BTitle LIKE ?;"
    return query, (f'%{book_name}%',)

def libViewId(id):
    query = "SELECT * FROM booklist WHERE bID LIKE ?;"
    return query, (f'%{id}%',)

def updateRole(role, email):
    query = "UPDATE auth SET role = ? WHERE emailAddress = ?;"
    return query, (role, email)

def insertNewBook(id,title,desc,author,publishOn,url,cover):
    query = "INSERT INTO bookList ( bID, BTitle, bDesc, bAuthor, bPublishedOn, bUrl, bCover ) VALUES ( ?, ?, ?, ?, ?, ?, ? );"
    return query, (id,title,desc,author,publishOn,url,cover)