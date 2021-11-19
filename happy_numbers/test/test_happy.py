import pytest
from happy_numbers import happy_numbers


def test_simple_case():
    assert happy_numbers.is_happy(1)


def test_unhappy():
    assert happy_numbers.is_happy(2) == False
