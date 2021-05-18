from config import get_conn, close_conn

table = 'weapon'


def select_all():
    query = "SELECT * FROM {0};".format(table)
    return query


def create_weapon(name, stock):
    query = "INSERT INTO {0} (name, stock) VALUES ('{1}', {2});".format(table, name, stock)
    return query


def update_weapon(name, modify_name, modify_stock):
    query = "UPDATE {0} SET name = '{1}', stock = {2} WHERE name = '{3}';".format(table, modify_name, modify_stock, name)
    return query


def delete_weapon(name):
    query = "DELETE FROM {0} WHERE name = '{1}';".format(table, name)
    return query

def mysql_select_weapon():
    conn = get_conn()
    query = select_all()
    result = conn.execute(query)
    close_conn(conn)
    return result


def mysql_create_weapon(name, stock):
    conn = get_conn()
    query = create_weapon(name, stock)
    result = conn.execute(query)
    close_conn(conn)
    return result


def mysql_update_weapon(name, modify_name, modify_stock):
    conn = get_conn()
    query = update_weapon(name, modify_name, modify_stock)
    result = conn.execute(query)
    close_conn(conn)
    return result


def mysql_delete_weapon(name):
    conn = get_conn()
    query = delete_weapon(name)
    print(query)
    result = conn.execute(query)
    close_conn(conn)
    return result