.PHONY: test

deps:
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

test:
	PYTHONPATH=. python3 tests/test_suite.py