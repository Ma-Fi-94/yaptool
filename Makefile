all: lint test docs

lint:
	importchecker *.py
	isort *.py
	yapf -i *.py

test:
	mypy *.py
	coverage run -m pytest
	coverage report -m

docs:
	pdoc plottingtools.py -d google -o ./docs
