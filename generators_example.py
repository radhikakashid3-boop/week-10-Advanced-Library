
import sys
from pathlib import Path

# Add the project root to Python's import path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from src.my_advanced_lib.core.generators import (
    count_up_to,
    fibonacci,
    batch_items,
    even_numbers,
)

print("Counting:", list(count_up_to(5)))
print("Fibonacci:", list(fibonacci(7)))
print("Batches:", list(batch_items([1, 2, 3, 4, 5], 2)))
print("Even numbers:", list(even_numbers([1, 2, 3, 4, 5, 6])))
