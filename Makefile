clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "*.log" -exec rm -rf {} \;

deps:
	pip install -r requirements.txt

setup:
	./manage.py migrate

run:
	./manage.py runserver

restart:
	dropdb generic_django_website
	createdb generic_django_website
	./manage.py migrate
	./manage.py createsuperuser
