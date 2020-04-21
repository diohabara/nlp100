init:
		pip install -r requirements.txt

freeze:
		rm requirements.txt
		pip freeze > requirements.txt

test:
		mypy nlp100/*py
		python -m unittest

.PHONY: init test