PYTHON		= python
SETUP		= $(PYTHON) setup.py

.PHONY: all
all:	
	python main.py


CHANGES.rst:
	git log --oneline --pretty=format:"* %ad: %s\n" --date=short > CHANGES.rst

.PHONY: init
init:	## Create Python virtual environment
	python3 -m venv _venv

.PHONY: reqs
reqs:	## Load Python requirements
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: test
test:
	python -m pytest

