
import re


def validate_email(email):
    """Check whether an email address has a valid format."""
    if not isinstance(email, str):
        return False

    pattern = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email))


def validate_password(password):
    """Check whether a password has at least 8 characters."""
    return isinstance(password, str) and len(password) >= 8


def validate_positive_number(value):
    """Check whether a number is positive."""
    if isinstance(value, bool):
        return False

    return (
        isinstance(value, (int, float))
        and value > 0
    )


def validate_not_empty(value):
    """Check whether a value is not empty."""
    if value is None:
        return False

    if isinstance(value, str):
        return bool(value.strip())

    return True



