import sqlite3 as sql

class Database():
    
    def __init__(self):
        self.conn = sql.connect('database.db')

        self.conn.execute('CREATE TABLE IF NOT EXISTS MENUS (ID INT, NAME TEXT, PRICE INT)')
        self.conn.row_factory = sql.Row
        self.cur = self.conn.cursor()

    def get_menus(self):
        response_data = []
        for row in self.cur.execute('SELECT * FROM MENUS'):
            response_data.append(dict(row))
        return response_data

    def create_menu(self, request_data):
        self.cur.execute('SELECT * FROM MENUS ORDER BY ROWID DESC LIMIT 1')
        id = self.cur.fetchone()[0] + 1
        name = request_data['name']
        price = request_data['price']
        self.cur.execute('INSERT INTO MENUS VALUES(?, ?, ?)', (id, name, price))
        self.conn.commit()
        request_data['id'] = id
        return request_data

    def update_menu(self, request_data):
        self.cur.execute('UPDATE MENUS SET name=?, price=? WHERE ID=?',
        (request_data['name'], request_data['price'], request_data['id']))
        self.conn.commit()
        return request_data

    def delete_menu(self, id):
        self.cur.execute('DELETE FROM MENUS WHERE ID=?', id)
        self.conn.commit()
        return self.get_menus()

    def __del__(self):
        self.conn.close()