
def count_up_to(n):
    """Generate numbers from 1 to n."""
    for i in range(1, n + 1):
        yield i


def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


def batch_items(items, batch_size):
    """Split items into batches."""
    if batch_size <= 0:
        raise ValueError("batch_size must be greater than zero")

    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]


def even_numbers(numbers):
    """Generate even numbers from an iterable."""
    for number in numbers:
        if number % 2 == 0:
            yield number

