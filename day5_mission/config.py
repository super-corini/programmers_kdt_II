db = {
    'user'     : 'root',		
    'password' : '0000',		
    'host'     : 'localhost',	
    'port'     : 3306,			
    'database' : 'hw'		
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"