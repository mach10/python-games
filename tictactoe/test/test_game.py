import pytest
from tictactoe import game

all_o_different_rows = [
    ([['x', 'o', 'o'], ['o', 'x', 'o'], ['o', 'x', 'o']], 'o wins'),
    ([['o', 'x', 'o'], ['o', 'o', 'o'], ['o', 'x', 'o']], 'o wins'),
    ([['o', 'x', 'o'], ['o', 'x', 'o'], ['o', 'o', 'o']], 'o wins')
]

all_x_different_rows = [
    ([['x', 'x', 'x'], ['o', 'x', 'o'], ['o', 'x', 'o']], 'x wins'),
    ([['o', 'x', 'o'], ['x', 'x', 'x'], ['o', 'x', 'o']], 'x wins'),
    ([['o', 'x', 'o'], ['o', 'x', 'o'], ['x', 'x', 'x']], 'x wins')
]

x_different_columns = [
    ([['x', 'o', 'x'], ['x', 'x', 'o'], ['x', 'x', 'o']], 'x wins'),
    ([['o', 'x', 'x'], ['x', 'x', 'o'], ['o', 'x', 'o']], 'x wins'),
    ([['x', 'o', 'x'], ['o', 'x', 'x'], ['x', 'o', 'x']], 'x wins')
]

o_different_columns = [
    ([['o', 'o', 'x'], ['o', 'x', 'o'], ['o', 'x', 'o']], 'o wins'),
    ([['o', 'o', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']], 'o wins'),
    ([['x', 'o', 'o'], ['o', 'x', 'o'], ['x', 'o', 'o']], 'o wins')
]

o_diagonals = [
    ([['o', 'o', 'x'], ['x', 'o', 'o'], ['x', 'x', 'o']], 'o wins'),
    ([['o', 'x', 'o'], ['x', 'o', 'x'], ['o', 'x', 'o']], 'o wins')
]

x_diagonals = [
    ([['x', 'o', 'x'], ['o', 'x', 'o'], ['x', 'x', 'x']], 'x wins'),
    ([['o', 'x', 'x'], ['x', 'x', 'o'], ['x', 'x', 'o']], 'x wins')
]


def test_no_winner():
    game_state = [['x', 'o', 'x'], ['o', 'x', 'o'], ['o', 'x', 'o']]
    undertest = game.Game(game_state)
    state = undertest.state()
    assert state == 'draw'


@pytest.mark.parametrize('test_input, expected', all_o_different_rows)
def test_o_wins_rows(test_input, expected):
    under_test = game.Game(test_input)
    assert expected == under_test.state()


@pytest.mark.parametrize('test_input, expected', all_x_different_rows)
def test_x_wins_rows(test_input, expected):
    under_test = game.Game(test_input)
    assert expected == under_test.state()


@pytest.mark.parametrize('test_input, expected', x_different_columns)
def test_x_wins_columns(test_input, expected):
    under_test = game.Game(test_input)
    state = under_test.state()
    assert expected == state


@pytest.mark.parametrize('test_input, expected', o_different_columns)
def test_o_wins_columns(test_input, expected):
    under_test = game.Game(test_input)
    state = under_test.state()
    assert expected == state


@pytest.mark.parametrize('test_input, expected', o_diagonals)
def test_o_diagonal(test_input, expected):
    under_test = game.Game(test_input)
    result = under_test.state()
    assert expected == result


@pytest.mark.parametrize('test_input, expected', x_diagonals)
def test_x_diagonal(test_input, expected):
    under_test = game.Game(test_input)
    result = under_test.state()
    assert expected == result