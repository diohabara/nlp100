init:
		python -m pip install --upgrade pip
		if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

freeze:
		rm requirements.txt
		pip freeze > requirements.txt

test:
		flake8
		mypy nlp100/*py
		python -m unittest

.PHONY: init test