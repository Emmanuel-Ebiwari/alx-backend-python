# This file contains a decorator that logs the SQL queries executed by a function.
def log_queries(func):
    def wrapper(*args, **kwargs):
        if args:
            print(f"Executing query: {args[0]}")
        result = func(*args, **kwargs)
        return result
    return wrapper

