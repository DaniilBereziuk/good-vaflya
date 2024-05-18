import sqlite3

connection = sqlite3.connect('my_db.db', 5)
cursor = connection.cursor()
# print(connection)
# print(cursor)

cursor.execute(
    'create table first_table (name TEXT);'
)
cursor.execute(
    'insert into first_table (name) values ("Nick");'
)
cursor.execute(
    'insert into first_table (name) values ("Babijonh");'
)
cursor.execute(
    'insert into first_table (name) values ("Sigma Bisnes");'
)


cursor.execute(
    'select rowid, name from first_table;'
)

connection.commit()
result = cursor.fetchall()
print(result)

cursor.execute(
    'select rowid, name from first_table where rowid = 3;'
)

connection.commit()
result = cursor.fetchall()
print(result)

cursor.execute(
    'update first_table set name="Ann" where rowid = 2;'
)

connection.commit()

cursor.execute(
    'select rowid, name from first_table;'
)

connection.commit()
result = cursor.fetchall()
print(result)

cursor.execute(
    'delete from first_table where rowid=4;'
)
connection.commit()

cursor.execute(
    'select rowid, name from first_table;'
)

connection.commit()
result = cursor.fetchall()
print(result)

cursor.execute(
    'drop table first_table;'
)
connection.commit()

connection.close()
