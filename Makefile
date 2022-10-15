all: lint test docs build

lint:
	importchecker *.py
	isort *.py
	yapf -i *.py
	pylint *.py

test:
	mypy *.py
	coverage run -m pytest
	coverage report -m

docs:
	pdoc plottingtools.py -d google -o ./docs

build:
	python -m build
	rm -r ./dist
