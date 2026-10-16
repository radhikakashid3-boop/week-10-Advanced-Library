
import time
from functools import wraps


def timer(func):
    """Calculate function execution time."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")

        return result

    return wrapper


def retry(max_attempts=3):
    """Retry a function if an exception occurs."""

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts - 1:
                        raise
                    print("Retrying function...")

        return wrapper

    return decorator


def cache_result(func):
    """Store and reuse previous results."""

    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            print("Using cached result")
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper

