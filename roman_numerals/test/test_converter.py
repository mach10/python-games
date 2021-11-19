import pytest

from roman_numerals import converter


@pytest.fixture
def undertest():
    return converter.Converter()


def test_converts_one(undertest):
    result = undertest.convert(1)
    assert 'I' == result


def test_converts_two(undertest):
    result = undertest.convert(2)
    assert 'II' == result


def test_converts_three(undertest):
    result = undertest.convert(3)
    assert 'III' == result


def test_converts_fifty_two(undertest):
    result = undertest.convert(52)
    assert 'LII' == result
