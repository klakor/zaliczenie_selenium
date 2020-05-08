.PHONY: test

deps:
	pip install -r test_requirements.txt

lint:
	flake8

test:
	PYTHONPATH=. python3 tests/test_suite.py