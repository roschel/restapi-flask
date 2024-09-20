APP = restapi

lint:
	@flake8 . --exclude .venv

test:
	@pytest tests -v --disable-warnings

compose:
	@docker compose build
	@docker compose up