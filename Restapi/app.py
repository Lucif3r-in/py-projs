from flask import Flask, request, jsonify

app = Flask(__name__)

book_list = [
    {
        "id": 0,
        "isbn": "9781593279509",
        "title": "Eloquent JavaScript, Third Edition",
        "subtitle": "A Modern Introduction to Programming",
        "author": "Marijn Haverbeke",
        "published": "2018-12-04T00:00:00.000Z",
        "publisher": "No Starch Press",
        "pages": 472,

    },
    {
        "id": 1,
        "isbn": "9781491943533",
        "title": "Practical Modern JavaScript",
        "subtitle": "Dive into ES6 and the Future of JavaScript",
        "author": "Nicolás Bevacqua",
        "published": "2017-07-16T00:00:00.000Z",
        "publisher": "O'Reilly Media",
        "pages": 334,

    },
    {
        "id": 2,
        "isbn": "9781593277574",
        "title": "Understanding ECMAScript 6",
        "subtitle": "The Definitive Guide for JavaScript Developers",
        "author": "Nicholas C. Zakas",
        "published": "2016-09-03T00:00:00.000Z",
        "publisher": "No Starch Press",
        "pages": 352,

    },
    {
        "id": 3,
        "isbn": "9781449365035",
        "title": "Speaking JavaScript",
        "subtitle": "An In-Depth Guide for Programmers",
        "author": "Axel Rauschmayer",
        "published": "2014-04-08T00:00:00.000Z",
        "publisher": "O'Reilly Media",
        "pages": 460,

    },
    {
        "id": 4,
        "isbn": "9781449331818",
        "title": "Learning JavaScript Design Patterns",
        "subtitle": "A JavaScript and jQuery Developer's Guide",
        "author": "Addy Osmani",
        "published": "2012-08-30T00:00:00.000Z",
        "publisher": "O'Reilly Media",
        "pages": 254,

    },
    {
        "id": 5,
        "isbn": "9798602477429",
        "title": "You Don't Know JS Yet",
        "subtitle": "Get Started",
        "author": "Kyle Simpson",
        "published": "2020-01-28T00:00:00.000Z",
        "publisher": "Independently published",
        "pages": 143,

    },
    {
        "id": 6,
        "isbn": "9781484200766",
        "title": "Pro Git",
        "subtitle": "Everything you neeed to know about Git",
        "author": "Scott Chacon and Ben Straub",
        "published": "2014-11-18T00:00:00.000Z",
        "publisher": "Apress; 2nd edition",
        "pages": 458,

    },
    {
        "id": 7,
        "isbn": "9781484242216",
        "title": "Rethinking Productivity in Software Engineering",
        "subtitle": "",
        "author": "Caitlin Sadowski, Thomas Zimmermann",
        "published": "2019-05-11T00:00:00.000Z",
        "publisher": "Apress",
        "pages": 310,

    }
]


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(book_list) > 0:
            return jsonify(book_list)
        else:
            'Nothing found', 404

    if request.method == 'POST':
        new_author = request.form['author'],
        new_publisher = request.form['publisher'],
        new_title = request.form['title'],
        iD = book_list[-1]['id'] + 1,

        new_obj = {
            'id': iD,
            'author': new_author,
            'publisher': new_publisher,
            'title': new_title
        }
        book_list.append(new_obj)
        return jsonify(book_list), 201


@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in book_list:
            if book['id'] == id:
                return jsonify(book)
            pass
    if request.method == 'PUT':
        for book in book_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['publisher'] = request.form['publisher']
                book['title'] = request.form['title']
                updated_book = {
                    'id': id,
                    'author': book['author'],
                    'publisher': book['publisher'],
                    'title': book['title'],
                }
                return jsonify(updated_book)
    if request.method == 'DELETE':
        for index, book in enumerate(book_list):
            if book['id'] == id:
                book_list.pop(index)
                return jsonify(book_list)


if __name__ == '__main__':
    app.run()
