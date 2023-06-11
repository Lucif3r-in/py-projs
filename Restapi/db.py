import pymysql

conn = pymysql.connect(
    host='sql12.freesqldatabase.com',
    database='sql12625216',
    user='sql12625216',
    password='PIAzgrctLX',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    publisher text NOT NULL,
    title text NOT NULL,
)"""

cursor.execute(sql_query)
conn.close()
