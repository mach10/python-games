import pytest
from factorial import factorial

def test_factorial_zero():
    result = factorial.make_factorial(0)
    assert 1 == result
