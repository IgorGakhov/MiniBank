freeze:
	pip freeze > requirements.txt

build-up:
	docker-compose up --build

up:
	docker-compose up

down:
	docker-compose down

exec-app:
	docker exec -it minibank_app bash

exec-db:
	docker exec -it minibank_db psql -U root minibank

exec-cache:
	docker exec -it minibank_cache redis-cli
