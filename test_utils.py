
import pytest
from src.my_advanced_lib.utils.validators import (
    validate_email,
    validate_password,
    validate_positive_number,
    validate_not_empty,
)


from src.my_advanced_lib.utils.serializers import (
    to_json,
    from_json,
    save_json,
    load_json,
)

from src.my_advanced_lib.utils.exceptions import (
    LibraryError,
    ValidationError,
    SerializationError,
    ConfigurationError,
)


def test_validate_email():
    assert validate_email("student@example.com") is True
    assert validate_email("invalid-email") is False
    assert validate_email(None) is False


def test_validate_password():
    assert validate_password("python123") is True
    assert validate_password("short") is False


def test_validate_positive_number():
    assert validate_positive_number(10) is True
    assert validate_positive_number(-5) is False
    assert validate_positive_number(True) is False


def test_validate_not_empty():
    assert validate_not_empty("Python") is True
    assert validate_not_empty("   ") is False
    assert validate_not_empty(None) is False


def test_json_conversion():
    data = {"course": "Python", "active": True}

    result = to_json(data)

    assert from_json(result) == data


def test_save_and_load_json(tmp_path):
    file_path = tmp_path / "data.json"
    data = {"language": "Python", "level": "Beginner"}

    save_json(data, file_path)

    assert load_json(file_path) == data


def test_custom_exceptions():
    with pytest.raises(ValidationError):
        raise ValidationError("Invalid input")

    assert issubclass(ValidationError, LibraryError)
    assert issubclass(SerializationError, LibraryError)
    assert issubclass(ConfigurationError, LibraryError)


from typing import Any, Callable, TypeVar

from src.my_advanced_lib.utils.types import (
    T,
    JSONValue,
    Decorator,
)


def test_type_aliases():
    assert isinstance(T, TypeVar)
    assert JSONValue is Any
    assert Decorator == Callable[..., Any]

def test_validate_email_invalid_inputs():
    assert validate_email(123) is False
    assert validate_email("invalid-email") is False
    assert validate_email("user@example.com") is True


def test_validate_password_invalid_inputs():
    assert validate_password(123) is False
    assert validate_password("short") is False
    assert validate_password("password123") is True


def test_validate_positive_number_invalid_inputs():
    assert validate_positive_number(True) is False
    assert validate_positive_number(-5) is False
    assert validate_positive_number(0) is False
    assert validate_positive_number(10) is True
    assert validate_positive_number(2.5) is True


def test_validate_not_empty_various_values():
    assert validate_not_empty(None) is False
    assert validate_not_empty("") is False
    assert validate_not_empty("   ") is False
    assert validate_not_empty("Python") is True
    assert validate_not_empty(0) is True
    assert validate_not_empty([]) is True