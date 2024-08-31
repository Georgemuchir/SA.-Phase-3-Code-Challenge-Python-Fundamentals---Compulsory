

def decorator_func(func):
    """Decorator that prints 'Decorator Applied' before calling the original function."""
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    """Applies the decorator_func to the provided function."""
    return decorator_func(func)
