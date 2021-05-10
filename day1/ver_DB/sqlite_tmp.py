import sqlite3 as sql

conn = sql.connect('database.db')
print('open success')

#conn.execute('CREATE TABLE MENUS (ID INT, NAME TEXT, PRICE INT)')
cur = conn.cursor()
#cur.execute('INSERT INTO MENUS (ID, NAME, PRICE) VALUES (?, ?, ?)',
#(1, 'Espresso', 3800))
a = conn.execute('SELECT * FROM MENUS')
print(a.fetchall())
#for A in a:
#    print(type(A[0]))
#print(a)
#conn.commit()
print('create success')
conn.close()