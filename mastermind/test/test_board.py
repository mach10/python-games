import pytest

from mastermind import mastermind


def test_all_correct_half_in_wrong_position():
    secret_code = ['red', 'red', 'orange', 'blue']
    guess = ['red', 'orange', 'red', 'blue']
    expected_score = ['black', 'black', 'white', 'white']
    undertest = mastermind.Board(secret_code)
    result = undertest.evaluate_guess(guess)
    assert result == expected_score


def test_black_white():
    secret_code = ['blue', 'blue', 'red', 'red']
    guess = ['blue', 'red', 'yellow', 'green']
    expected_score = ['black', 'white']
    undertest = mastermind.Board(secret_code)
    result = undertest.evaluate_guess(guess)
    assert result == expected_score


def test_white():
    secret_code = ['green', 'green', 'green', 'blue']
    guess = ['blue', 'red', 'red', 'orange']
    expected_score = ['white']
    undertest = mastermind.Board(secret_code)
    result = undertest.evaluate_guess(guess)
    assert result == expected_score


def test_empty():
    secret_code = ['green', 'green', 'yellow', 'orange']
    guess = ['red', 'red', 'purple', 'blue']
    expected_score = []
    undertest = mastermind.Board(secret_code)
    result = undertest.evaluate_guess(guess)
    assert result == expected_score


def test_winner():
    secret_code = ['red', 'red', 'green', 'orange']
    guess = ['red', 'red', 'green', 'orange']
    expected_score = 'Winner!'
    undertest = mastermind.Board(secret_code)
    result = undertest.evaluate_guess(guess)
    assert result == expected_score
