import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=()):
        self.query = query
        self.params = params
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        cursor = self.connection.cursor()
        cursor.execute(self.query, self.params)
        return cursor.fetchall()
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
        return True
    
query = "SELECT * FROM users WHERE age > ?"
params = (25,)
    
with ExecuteQuery('users.db', query, params) as result:
    print(result)