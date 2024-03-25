# -*- coding: utf-8 -*-
import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('example.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаем новую таблицу
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL)''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()
