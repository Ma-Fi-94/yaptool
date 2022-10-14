# Coding style 
yapf -i plottingtools.py
yapf -i test_plottingtools.py

# Type checking
mypy plottingtools.py
mypy test_plottingtools.py

# Test suite incl. coverage report
coverage run -m pytest
coverage report -m

# Generate docs
pdoc plottingtools.py -d google -o ./docs

