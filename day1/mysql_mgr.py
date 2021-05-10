from config import get_conn, close_conn

table = 'menu'

def insert_sql(name, price):
    query = "INSERT INTO {0} (name, price) VALUES ('{1}', {2});".format(table, name, price)
    print("[MySQL - INSERT]", query)
    return query


def select_all_sql():
    query = "SELECT * FROM {0};".format(table)
    print("[MySQL - SELECT]", query)
    return query

def select_sql(menu_id):
    query = "SELECT * FROM {0} WHERE id = {1};".format(table, menu_id)
    print("[MySQL - SELECT]", query)
    return query


def delete_sql(menu_id): 
    query = "DELETE FROM {0} WHERE id = {1};".format(table, menu_id)
    print("[MySQL - DELETE]", query)
    return query


def update_sql(menu_id, modified_name, modified_price):
    query = "UPDATE {0} SET name = '{1}', price = {2} WHERE id = {3};".format(table, modified_name, modified_price, menu_id)
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


def mysql_select(menu_id):
    conn = get_conn()
    query = select_sql(menu_id)    
    result = conn.execute(query)
    close_conn(conn)
    return result


def mysql_delete(menu_id):
    conn = get_conn()
    query = delete_sql(menu_id)    
    result = conn.execute(query)
    close_conn(conn)
    return result


def mysql_update(menu_id, modified_name, modified_price):
    conn = get_conn()
    query = update_sql(menu_id, modified_name, modified_price)    
    result = conn.execute(query)
    close_conn(conn)
    return result
