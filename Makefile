.PHONY:install
install:
	poetry install


.PHONY:install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install 


.PHONY: lint
lint:
	poetry run pre-commit run --all-files


.PHONY:migrate
migrate:
	poetry run python -m core.manage migrate


.PHONY:migrations
migrations:
	poetry run python -m core.manage makemigrations


.PHONY:collectstatic
collectstatic:
	poetry run python -m core.manage collectstatic


.PHONY:runserver
runserver:
	poetry run python -m core.manage runserver_plus


.PHONY:superuser
superuser:
	poetry run python -m core.manage createsuperuser


.PHONY:test
test:
	poetry run python -m core.manage test


.PHONY:huey
huey:
	poetry run python -m core.manage run_huey


.PHONY:setup
setup: install migrations migrate ;


.PHONY:push-update
push-update: migrations migrate collectstatic ;
