start:
	poetry run python3 manage.py runserver
lint:
	poetry run flake8 hexlet_django_blog

makemigrations:
	poetry run python3 manage.py makemigrations

migrate:
	poetry run python3 manage.py migrate

.PHONY: start, lint, makemigrations

