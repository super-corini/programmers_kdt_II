import sqlite3 as sql

class Database():
    
    def __init__(self):
        self.conn = sql.connect('database.db')

        self.conn.execute('CREATE TABLE IF NOT EXISTS WEAPONS (NAME TEXT, STOCK INT)')
        self.conn.row_factory = sql.Row
        self.cur = self.conn.cursor()

    def get_weapons(self):
        response_data = []
        for row in self.cur.execute('SELECT * FROM WEAPONS'):
            response_data.append(dict(row))
        return response_data

    def create_weapon(self, request_data):
        name = request_data['name']
        stock = request_data['stock']
        self.cur.execute('INSERT INTO WEAPONS VALUES(?, ?)', (name, stock))
        self.conn.commit()
        return self.get_weapons()

    def update_weapon(self, request_data):
        self.cur.execute('UPDATE WEAPONS SET NAME=?, STOCK=? WHERE NAME=?',
        (request_data['name'], request_data['stock'], request_data['name']))
        self.conn.commit()
        return self.get_weapons()

    def delete_weapon(self, name):
        print(name)
        self.cur.execute('DELETE FROM WEAPONS WHERE NAME=?', (name,))
        self.conn.commit()
        return self.get_weapons()

    def __del__(self):
        self.conn.close()