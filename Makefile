lint:
	poetry run pysen run format
	poetry run pysen run lint
watch:
	poetry run ptw .
test:
	poetry run pytest

.PHONY: init test