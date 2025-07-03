# Django CRUD + WebSocket Project

Полноценное Django-приложение с реализацией:

- CRUD-интерфейсов для моделей
- HTML-шаблонов для каждой сущности
- WebSocket-уведомлений через Django Channels
- Документацией к API (Swagger)
- Возможностью запуска через Docker и Makefile

---

## 🔧 Подготовка перед запуском

Перед первым запуском необходимо создать файл `.env` в корне проекта со следующими переменными окружения:

```env
POSTGRES_DB=your_database_name
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_PORT=5432
POSTGRES_HOST=postgres

DJANGO_PORT=8000
DJANGO_SECRET_KEY=your_secret_key
DJANGO_PROFILE=local
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_CSRF_TRUSTED=http://localhost:8000/
REDIS_URL=redis://redis:6379/0
```

---

## ⚙️ Настройки

Конфигурация проекта разделена на два окружения:

- `settings/local/` — для разработки
- `settings/prod/` — для продакшена

Окружение выбирается переменной `DJANGO_PROFILE` в `.env`.

---

## 🚀 Запуск через Docker

Для удобства в проекте используется `Makefile`. Он автоматизирует запуск и работу с контейнерами.

### Основные команды:

```bash
# Запуск сервисов хранения (PostgreSQL, Redis и др.)
make storages

# Запуск Django-приложения (если storages ещё не запущены, они поднимутся автоматически)
make app

# Применить миграции и создать суперпользователя
make migrate
make superuser

# Открыть приложение
# http://localhost:8000/
```

---

## 🧰 Полный список команд Makefile

| Команда                     | Описание                                                       |
|----------------------------|----------------------------------------------------------------|
| `make storages`            | Запуск сервисов хранения (PostgreSQL, Redis и т.д.)            |
| `make storages-down`       | Остановка всех сервисов хранения                               |
| `make storages-logs`       | Просмотр логов хранилищ                                        |
| `make postgres`            | Подключение к Postgres внутри контейнера                       |
|                            |                                                                |
| `make app`                 | Запуск Django-приложения                                       |
| `make app-down`            | Остановка приложения                                           |
| `make app-logs`            | Просмотр логов приложения                                      |
|                            |                                                                |
| `make migrate`             | Выполнение миграций                                            |
| `make migrations`          | Создание миграций                                              |
| `make superuser`           | Создание суперпользователя                                     |
| `make collectstatic`       | Сбор статики внутри контейнера                                 |

---

## 📎 Доступ к приложению

После запуска приложение доступно по адресу:

```
http://localhost:8000/
```

Настроить адрес можно в файле `docker_compose/app.yaml`.

---

## ✅ Возможности

- Полный CRUD для моделей: `Supplier`, `Category`, `Product` и других
- HTML-шаблоны (templates) для всех операций
- WebSocket-уведомления при действиях с сущностями
- Адаптировано под продакшен и dev-среду

---

## 📦 Требования (если запускать без Docker)

- Python 3.12+
- PostgreSQL
- Redis
- Установленные зависимости из `pyproject.toml`

---

\
