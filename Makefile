APP = restapi

flake:
	@flake8 . --exclude "venv tralha.py"
compose:
	@docker compose build
	@docker compose up
requirements:
	@pip freeze > requirements.txt
