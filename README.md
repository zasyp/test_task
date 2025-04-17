# FastAPI и PostgreSQL в Docker

Докеризированное FastAPI-приложение с базой данных PostgreSQL.

## Требования

- Docker
- Docker Compose (v2+)

## Быстрый старт

1. **Клонируйте репозиторий**:
   ```bash
   git clone [ваш-url-репозитория]
   cd ваш-репозиторий
   ```

2. **Соберите и запустите сервисы**:
   ```bash
   docker compose up --build
   ```

3. **Доступ к эндпоинтам**:
   - Приложение: `http://localhost:8000`
   - Документация API: `http://localhost:8000/docs`
   - PostgreSQL: доступна на порту `5432`

## Настройка окружения

1. Создайте файл `.env` (используйте `.env.example` как шаблон):
   ```env
   DATABASE_URL=postgresql://user:pass@db:5432/mydb
   ```

2. Пересоберите контейнеры после изменения `.env`:
   ```bash
   docker compose up --build
   ```

## Основные команды

- Остановить контейнеры: `docker compose down`
- Данные БД: хранятся в Docker-томе `postgres_data`
