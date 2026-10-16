
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from src.my_advanced_lib.utils.validators import (
    validate_email,
    validate_password,
    validate_positive_number,
    validate_not_empty,
)

from src.my_advanced_lib.utils.serializers import (
    to_json,
    from_json,
)

print("Email valid:", validate_email("student@example.com"))
print("Password valid:", validate_password("python123"))
print("Positive number:", validate_positive_number(25))
print("Not empty:", validate_not_empty("Python"))

data = {
    "course": "Python",
    "level": "Beginner",
    "active": True,
}

json_data = to_json(data)
print("JSON:", json_data)
print("Python data:", from_json(json_data))


from src.my_advanced_lib.utils.exceptions import (
    LibraryError,
    ValidationError,
)

try:
    raise ValidationError("Invalid input data")
except LibraryError as error:
    print("Custom exception:", error)
