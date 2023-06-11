from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = pymysql.connect(host='sql12.freesqldatabase.com',
                               database='sql12625216',
                               user='sql12625216',
                               password='PIAzgrctLX',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
    except pymysql.error as e:
        print(e)
    return conn


@app.route("/books", methods=["GET", "POST"])
def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM book")
        books = [
            dict(id=row['id'], author=row['author'],
                 publisher=row['publisher'], title=row['title'])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == "POST":
        new_author = request.form["author"]
        new_publisher = request.form["publisher"]
        new_title = request.form["title"]
        sql = """INSERT INTO book (author, language, title)
                 VALUES (%s, %s, %s)"""
        cursor = cursor.execute(sql, (new_author, new_publisher, new_title))
        conn.commit()
        return f"Book with the id: 0 created successfully", 201


@app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong", 404

    if request.method == "PUT":
        sql = """UPDATE book
                SET title=?,
                    author=?,
                    publisher=?
                WHERE id=? """

        author = request.form["author"]
        publisher = request.form["publisher"]
        title = request.form["title"]
        updated_book = {
            "id": id,
            "author": author,
            "publisher": publisher,
            "title": title,
        }
        conn.execute(sql, (author, publisher, title, id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == "DELETE":
        sql = """ DELETE FROM book WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The book with id: {} has been ddeleted.".format(id), 200


if __name__ == "__main__":
    app.run(debug=True)
