import sqlite3
connection = sqlite3.connect('books.db')

import pandas as pd
pd.options.display.max_columns = 10
lastname = pd.read_sql('SELECT last, id FROM authors ORDER BY last DESC', connection, index_col=['id'])
print(lastname)
print()

titles = pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
print(titles)
print()

inner = pd.read_sql("SELECT author_ISBN.isbn, first, last, title, copyright FROM (author_ISBN INNER JOIN authors ON author_ISBN.id = authors.id) INNER JOIN titles ON author_ISBN.isbn = titles.isbn WHERE last LIKE 'D%' ORDER BY title", connection)
print(inner)
print()

cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""")
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))
print()

cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES (6, '0134111222')""")
print(pd.read_sql('SELECT id, isbn FROM author_ISBN WHERE id=6', connection, index_col=['id']))
print()

cursor = cursor.execute("""INSERT INTO titles (title, isbn, edition, copyright) VALUES ("Linkang Wang's Book", '0134111222', 1, 2021)""")
print(pd.read_sql('SELECT id, title, titles.isbn FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn WHERE id=6', connection))
print()
