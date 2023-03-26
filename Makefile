start:migrate  
	poetry run python3 manage.py runserver
lint:
	poetry run flake8 hexlet_django_blog

migrate:       
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
shell:
	poetry run python3 manage.py shell

PHONY: start, lint, migrate, shell

