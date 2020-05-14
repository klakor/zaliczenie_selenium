.PHONY: test

deps:
	pip install -r requirements.txt

test:
	PYTHONPATH=. python3 tests/test_suite.py