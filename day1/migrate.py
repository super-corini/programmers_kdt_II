import sqlite3
from sqlite3 import Error


def create_connection(dbpath):
    conn = None
    try:
        conn = sqlite3.connect(dbpath)
    except Error as e:
        print(e)

    return conn


def create_table(cursor):
    str_create_table = ("CREATE TABLE IF NOT EXISTS menus ("
                        "   id INTEGER PRIMARY KEY,"
                        "   name TEXT NOT NULL,"
                        "   price INTEGER NOT NULL"
                        ");")
    try:
        cursor.execute(str_create_table)
    except Error as e:
        print(e)


def main():
    conn = create_connection('./day1.sqlite')
    if conn:
        cursor = conn.cursor()
        create_table(cursor)


if __name__ == "__main__":
    main()
