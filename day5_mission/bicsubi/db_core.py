import sqlite3


class BicsubiDb:
    def __init__(self, db_path=None):
        if not db_path:
            return
        self.path = db_path
        self.sql_scheme = {'info': ("CREATE TABLE IF NOT EXISTS info ("
                                    "   id INTEGER PRIMARY KEY,"
                                    "   key_ TEXT NOT NULL UNIQUE,"
                                    "   val_ TEXT NOT NULL"
                                    ");"),
                           'weapon': ("CREATE TABLE IF NOT EXISTS weapon ("
                                      "   id INTEGER PRIMARY KEY,"
                                      "   name TEXT NOT NULL UNIQUE,"
                                      "   stock INTEGER NOT NULL"
                                      ");")}
        self.create_table()

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.path)
            conn.set_trace_callback(print)
        except sqlite3.Error as e:
            print(e)
        return conn, conn.cursor()

    def create_table(self):
        conn, cursor = self.create_connection()
        try:
            for table in self.sql_scheme:
                cursor.execute(self.sql_scheme[table])
        except sqlite3.Error as e:
            print(e)

    def get_info(self, item):
        conn, cursor = self.create_connection()
        cursor.execute("SELECT val_ FROM info WHERE key_ = ?;", (item,))
        ret = cursor.fetchone()[0]
        conn.close()
        return ret

    def weapon_create(self, name, stock):
        conn, cursor = self.create_connection()
        cursor.execute("INSERT INTO weapon (name, stock) VALUES (?, ?);",
                       (name, stock))
        conn.commit()
        conn.close()

    def weapon_list_weapons(self):
        conn, cursor = self.create_connection()
        cursor.execute("SELECT name, stock FROM weapon;")
        ret = dict()
        for row in cursor.fetchall():
            ret[row[0]] = int(row[1])
        return ret

    def weapon_update(self, **kwargs):
        name = kwargs['name']
        if not self.weapon_check_(name):
            return False
        target = ''
        values = []
        kwargs['name'] = kwargs.pop('new_name') if kwargs['new_name'] else name
        for k in ('name', 'stock'):
            if k in kwargs and kwargs[k]:
                target += f'{k} = ?,'
                values.append(kwargs[k])
        target = target[:-1]
        values.append(name)
        conn, cursor = self.create_connection()
        cursor.execute(f"UPDATE weapon SET {target} WHERE name = ?;",
                       tuple(values))
        conn.commit()
        conn.close()
        return True

    def weapon_delete(self, name):
        if not self.weapon_check_(name):
            return False
        conn, cursor = self.create_connection()
        cursor.execute("DELETE FROM weapon WHERE name = ?;", (name,))
        conn.commit()
        conn.close()
        return True

    def weapon_check_(self, name):
        conn, cursor = self.create_connection()
        cursor.execute("SELECT 1 FROM weapon WHERE name = ?;", (name,))
        ret = False
        if cursor.fetchone():
            ret = True
        conn.close()
        return ret

    def info_read(self, key):
        conn, cursor = self.create_connection()
        cursor.execute("SELECT val_ FROM info WHERE key_ = ?;", (key,))
        ret = {}
        if cursor.fetchone():
            ret = cursor.fetchone()[0]
        conn.close()
        return ret

    def info_write(self, key, val):
        conn, cursor = self.create_connection()
        cursor.execute("INSERT INTO info (key_, val_) VALUES (?, ?);", (key, val))
        conn.commit()
        conn.close()

    def info_update(self, key, val):
        if not self.info_read(key):
            return False
        conn, cursor = self.create_connection()
        cursor.execute("UPDATE info SET val_ = ? WHERE key_ = ?;", (val, key))
        conn.commit()
        conn.close()
        return True
