init:
		pip install -r requirements.txt

freeze:
		rm requirements.txt
		pip freeze > requirements.txt

test:
		flake8
		mypy nlp100/*py
		python -m unittest

.PHONY: init test