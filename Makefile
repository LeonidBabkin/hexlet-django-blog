start:
	poetry run python3 manage.py runserver
lint:
	poetry run flake8 hexlet_django_blog

.PHONY: start, lint
