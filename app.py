from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)

SWAGGER_URL = '/api-docs' 
API_URL = '/static/api.yaml' 
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Book API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error":"Resource not found"}), 404


books = []


'''
Add a new book
Each book should have the following details:
● Title (required)
● Author (required)
● Published Year (required)
● ISBN (required)
● Genre (optional)
'''
@app.route("/books/add-book", methods = ["POST"])
def add_book():
    title = request.json.get("title")
    author = request.json.get("author")
    published_year = request.json.get("published_year")
    isbn = request.json.get("isbn")
    genre = request.json.get("genre", None)
    if not title or not author or not published_year or not isbn:
        return jsonify({"error": "Missing required fields: 'title', 'author', 'published_year', 'isbn' are required"}), 400
    
    book = {
        "id" : len(books) + 1,
        "title" : title,
        "author": author,
        "published_year": published_year,
        "isbn": isbn,
        "genre": genre
    }
    books.append(book)
    return jsonify(book), 201

'''
List all books
Return a list of all books with their details.
'''

@app.route("/books/list-all-books", methods = ["GET"])
def get_books():
    return jsonify(books)





'''
Search for books
Allow filtering books by one or more of the following:
● Author
● Published Year
● Genre
'''

@app.route("/books/search-books", methods = ["GET"])
def search_books():
    '''
    request.args is the best practice in the search queries like 
    https/........?author=example
    '''
    author = request.args.get("author")
    published_year = request.args.get("published_year")
    genre = request.args.get("genre")
    filteredBooks = []
    for book in books:
        if author == book["author"]:
            filteredBooks.append(book)
    
    for book in books:
        if published_year == book["published_year"]:
            filteredBooks.append(book)
    
    for book in books:
        if genre == book["genre"]:
            filteredBooks.append(book)
    
    return jsonify({"Filtered books":filteredBooks})

    





'''
Update book details by ISBN
Update one or more details of a specific book using its ISBN.
'''

@app.route("/books/<int:isbn>", methods = ["PUT"])
def update_book(isbn):
    book = next((b for b in books if b["isbn"] == isbn), None)
    if book is None:
        return jsonify({"error":"book not found"}), 404
    book["title"] = request.json.get("title", book["title"])
    book["author"] = request.json.get("author", book["author"])
    return jsonify(book)


'''
Delete a book by ISBN
Remove a specific book from the library using its ISBN.
'''

@app.route("/books/<int:isbn>", methods = ["DELETE"])
def delete_book(isbn):
    global books
    book = next((b for b in books if b["isbn"] == isbn), None)
    if book is None:
        return jsonify({"error": "book not found"}), 404
    
    
    books = [b for b in books if b["isbn"] != isbn] 
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)