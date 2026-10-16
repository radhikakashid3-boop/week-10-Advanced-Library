
from src.my_advanced_lib.core.decorators import (
    timer,
    retry,
    cache_result,
)


def test_timer():
    @timer
    def add(a, b):
        return a + b

    assert add(2, 3) == 5


def test_retry_success():
    @retry(max_attempts=3)
    def greet():
        return "Hello"

    assert greet() == "Hello"


def test_cache_result():
    calls = []

    @cache_result
    def calculate(number):
        calls.append(number)
        return number * 2

    assert calculate(5) == 10
    assert calculate(5) == 10
    assert len(calls) == 1

    
import pytest
from src.my_advanced_lib.core.decorators import retry


def test_retry_succeeds_after_one_failure():
    calls = {"count": 0}

    @retry(max_attempts=3)
    def unstable_function():
        calls["count"] += 1

        if calls["count"] == 1:
            raise ValueError("Temporary error")

        return "Success"

    result = unstable_function()

    assert result == "Success"
    assert calls["count"] == 2


def test_retry_raises_after_all_attempts_fail():
    calls = {"count": 0}

    @retry(max_attempts=3)
    def failing_function():
        calls["count"] += 1
        raise ValueError("Always fails")

    with pytest.raises(ValueError, match="Always fails"):
        failing_function()

    assert calls["count"] == 3

