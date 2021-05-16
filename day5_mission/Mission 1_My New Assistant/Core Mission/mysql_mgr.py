from config import get_conn, close_conn

table = 'weapon'


def insert_sql(name, stock):
    query = "INSERT INTO {0} (name, stock) VALUES ('{1}', {2});".format(table, name, stock)
    print("[MySQL - INSERT]", query)
    return query


def select_all_sql():
    query = "SELECT * FROM {0};".format(table)
    print("[MySQL - SELECT]", query)
    return query

def select_sql(weapon_name):
    query = "SELECT * FROM {0} WHERE name = '{1}';".format(table, weapon_name)
    print("[MySQL - SELECT]", query)
    return query


def delete_sql(weapon_name):
    query = "DELETE FROM {0} WHERE name = '{1}';".format(table, weapon_name)
    print("[MySQL - DELETE]", query)
    return query


def update_sql(weapon_name, modified_name, modified_stock):
    query = "UPDATE {0} SET name = '{1}', stock = {2} WHERE name = '{3}';"\
        .format(table, modified_name, modified_stock, weapon_name)
    print("[MySQL - UPDATE]", query)
    return query


def mysql_insert(obj, values):
    conn = get_conn()   
    query = insert_sql(obj, values)
    result = conn.execute(query)
    close_conn(conn)
    return result


def mysql_select_all():
    conn = get_conn()
    query = select_all_sql()    
    result = conn.execute(query)
    close_conn(conn)
    return result


def mysql_select(weapon_name):
    conn = get_conn()
    query = select_sql(weapon_name)
    result = conn.execute(query)
    close_conn(conn)
    return result


def mysql_delete(weapon_name):
    conn = get_conn()
    query = delete_sql(weapon_name)
    result = conn.execute(query)
    close_conn(conn)
    return result


def mysql_update(weapon_name, modified_name, modified_stock):
    conn = get_conn()
    query = update_sql(weapon_name, modified_name, modified_stock)
    result = conn.execute(query)
    close_conn(conn)
    return result
