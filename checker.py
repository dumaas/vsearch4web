from functools import wraps


from flask import session


def check_logged_in(func):
    """Decorator that checks if logged in"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if "logged_in" in session:
            return func(*args, **kwargs)
        return "You are NOT logged in."

    return wrapper
