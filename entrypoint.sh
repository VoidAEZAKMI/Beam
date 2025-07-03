#!/bin/sh

# Функция ожидания доступности порта
wait_for_port() {
    local host="$1"
    local port="$2"
    local timeout=10
    local start_time=$(date +%s)

    # Попробовать использовать nc, если установлен
    local nc_command="nc"
    type "$nc_command" >/dev/null 2>&1 || nc_command="ncat"

    while ! $nc_command -z "$host" "$port" >/dev/null 2>&1; do
        sleep 1
        local current_time=$(date +%s)
        local elapsed_time=$((current_time - start_time))
        echo "trying to connect to PG at $host:$port"

        if [ $elapsed_time -ge $timeout ]; then
            echo "Unable to connect to Postgres on $host:$port"
            exit 1
        fi
    done
}

# Ожидание доступности порта PostgreSQL
wait_for_port "$POSTGRES_HOST" "$POSTGRES_PORT"

# Запуск Django-приложения (слушаем 8000)
python manage.py runserver 0.0.0.0:8000
# daphne -p 8000 core.app.asgi:application