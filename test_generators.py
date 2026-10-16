
from src.my_advanced_lib.core.generators import (
    count_up_to,
    fibonacci,
    batch_items,
    even_numbers,
)


def test_count_up_to():
    assert list(count_up_to(4)) == [1, 2, 3, 4]


def test_fibonacci():
    assert list(fibonacci(6)) == [0, 1, 1, 2, 3, 5]


def test_batch_items():
    assert list(batch_items([1, 2, 3, 4, 5], 2)) == [
        [1, 2],
        [3, 4],
        [5],
    ]


def test_even_numbers():
    assert list(even_numbers([1, 2, 3, 4])) == [2, 4]


import pytest
from src.my_advanced_lib.core.generators import batch_items


def test_batch_items_zero_size():
    with pytest.raises(
        ValueError,
        match="batch_size must be greater than zero"
    ):
        list(batch_items([1, 2, 3], 0))


def test_batch_items_negative_size():
    with pytest.raises(
        ValueError,
        match="batch_size must be greater than zero"
    ):
        list(batch_items([1, 2, 3], -2))

