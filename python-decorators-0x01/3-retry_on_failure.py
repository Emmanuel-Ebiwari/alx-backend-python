import time
import sqlite3 
import functools

#### paste your with_db_decorator here

def with_db_connection(func):
    # Preserves the original function's metadata (name, docstring, etc.)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            # Inject conn into the function's keyword arguments
            result = func(*args, **kwargs, conn=conn)
            return result
        finally:
            conn.close()
    return wrapper

def retry_on_failure(retries=3, delay=1):
    """Decorator to retry a function call on failure."""
    def decorator(func):
        # Preserves the original function's metadata (name, docstring, etc.)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < retries - 1:
                        print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"All attempts failed: {e}")
                        raise
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)