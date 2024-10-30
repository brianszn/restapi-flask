APP = restapi

flake:
	@flake8 . --exclude "venv tralha.py"
compose:
	@docker compose up

