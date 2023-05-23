1) Создать копию `api/.env_example` и переименовать ее  в `api/.env`. Внести данные о БД
2) `cd api`
3) `pip install -r requirements.txt`
4) Создать папку `versions` в `api/migrations`
5) `alembic revision --autogenerate -m 'init'`
6) `alembic upgrade head`
7) `cd ../frontend`
8) `npm install`
9) Запуск сервера api - `uvicorn main:app --reload` (из папки `api`)
10) Запуск сервера frontend - `npm run serve` (из папки `frontend`)
