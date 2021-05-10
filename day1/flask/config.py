db = {
    'user'     : 'root',		
    'password' : '0000',		
    'host'     : 'localhost',	
    'port'     : 5000,			
    'database' : 'minitter'		
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"