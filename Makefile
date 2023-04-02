start:migrate  
	poetry run python3 manage.py runserver
lint:
	poetry run flake8 hexlet_django_blog
migrate:       
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
shell:
	poetry run python3 manage.py shell	
shellplus:
           poetry run python3 manage.py shell_plus	   
validatetemplates:
                   poetry run python3 manage.py validate_templates
graphmodels:
             poetry run python3 manage.py graph_models
showurls:
          poetry run python3 manage.py show_urls

PHONY: start, lint, migrate, shell, shellplus, validatetemplates, graphmodels, showurls

