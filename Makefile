.PHONY: test

deps:
	pip install -r test_requirements.txt

test:
	PYTHONPATH=. python3 tests/test_suite.py