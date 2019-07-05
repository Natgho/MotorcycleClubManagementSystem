docker:
	docker-compose up --build

install:
	pip install -r requirements.txt

migrations:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver 127.0.0.1:8000
