yapf -i plottingtools.py
yapf -i test_plottingtools.py
mypy plottingtools.py
mypy test_plottingtools.py
py.test --cov-report term-missing --cov=. -v
