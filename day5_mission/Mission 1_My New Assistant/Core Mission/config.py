from sqlalchemy import create_engine

db = {
    'user'      : 'root',
    'password'  : '',
    'host'      : 'localhost',
    'port'      : '3306',
    'database'  : 'bicsubi'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

engine = create_engine(DB_URL,
                       convert_unicode=False,
                       pool_size=100,
                       max_overflow=0,
                       pool_recycle=3600,
                       encoding='utf-8'
                       )

def get_conn():
    return engine.connect()


def close_conn(conn):
    conn.close()
    return
