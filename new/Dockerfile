FROM python:latest

# Установка зависимостей
RUN pip install telebot

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование исходного кода приложения в образ
COPY . .

# Команда для выполнения миграций
CMD ["python", "migrate_script.py"]

