.PHONY: pip_dev run test_roman_numerals test_tictactoe test_mastermind test_happy_numbers test_factorial test_divisor test_analytics

env pip_dev:
	python -m venv env
	env/bin/pip install --upgrade pip
	env/bin/pip install -r requirements.txt

test_roman_numerals: env
	env/bin/pytest roman_numerals/test

test_tictactoe: env
	env/bin/pytest tictactoe/test

test_mastermind: env
	env/bin/pytest mastermind/test

test_happy_numbers: env
	env/bin/pytest happy_numbers/test

test_factorial: env 
	env/bin/pytest factorial/test 

test_divisor: env
	env/bin/pytest divisor/test

test_analytics: env
	env/bin/pytest analytics/test

clean:
	rm -rf env