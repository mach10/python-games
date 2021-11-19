import pytest
from factorial import factorial

def test_fails_with_string_input():
    try:
        factorial.make_factorial('garbage')
        assert 1 == 2
    except IndexError as e:
        assert True

def test_fails_with_negative_number():
    try:
        factorial.make_factorial(-23)
        assert 1 == 2
    except TypeError as e:
        assert True

def test_factorial_zero():
    result = factorial.make_factorial(0)
    assert 1 == result
