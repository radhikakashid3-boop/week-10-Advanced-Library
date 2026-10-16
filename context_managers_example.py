
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from src.my_advanced_lib.core.context_managers import (
    SafeFileHandler,
    temporary_setting,
    temporary_directory,
)

# Example 1: SafeFileHandler
file_path = ROOT_DIR / "example.txt"

with SafeFileHandler(file_path, "w") as file:
    file.write("Hello from Context Manager!")

with SafeFileHandler(file_path, "r") as file:
    print("File content:", file.read())


# Example 2: temporary_setting
class Student:
    name = "Radhika"


student = Student()

print("Original name:", student.name)

with temporary_setting(student, "name", "Python Student"):
    print("Temporary name:", student.name)

print("Restored name:", student.name)


# Example 3: temporary_directory
with temporary_directory(ROOT_DIR) as directory:
    print("Temporary directory exists:", directory.exists())

print("Temporary directory exists after exit:", directory.exists())
