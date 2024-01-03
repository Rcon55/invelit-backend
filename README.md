#### Создать контейнеры
docker compose build

#### Запустить контейнеры
docker compose up 

#### Создать миграцию
docker-compose run app alembic revision --autogenerate -m "migration name"

#### Запустить миграцию
docker-compose run app alembic upgrade head
