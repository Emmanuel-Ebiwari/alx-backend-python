import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

# This file contains a decorator that logs the SQL queries executed by a function.
def log_queries(func):
    @functools.wraps(func) # Preserves the original function's metadata (name, docstring, etc.)
    def wrapper(*args, **kwargs):
        query = args[0] if args else kwargs.get('query', '<no query>')
        print(f"{datetime.now()}: Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")


