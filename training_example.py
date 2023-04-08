import os
import psycopg2

"""Полезная информация
подключиться к postgresql можно с помощью команды - sudo -u postgres psql
подключиться к БД - \connect <наименование бд>
посмотреть наличение таблиц - \dt
посмотреть содержимое таблиц - TABLE <наименование таблицы>;TAB """

try:
    # Подключение в базен
    connection = psycopg2.connect(
    host = "127.0.0.1",
    port = "8090",
    user = "postgres",
    password ="postgres",
    database = "postgres"
    )
    connection.autocommit = True
    """Проверка версии БД Postgresql"""
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print("Server version: {}".format(cursor.fetchone()))

    """Создание таблицы в БД db_base"""
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                nick_name varchar(50) NOT NULL);"""
        )
        print("[INFO] Таблица успешно создана")

    """Добавление данных в таблицу"""
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (first_name, nick_name) VALUES
            ('Alex', 'politex')"""
        )
        print("[INFO] Добавление информации в таблицу пройдено успешно")

    """Вывод информации из таблицы users"""
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT nick_name FROM users WHERE first_name = 'Alex';"""
        )
        print(cursor.fetchone())

    """Удаление всей таблицы целиком"""
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users;"""
        )
        print("[INFO] Таблица users успешно удалена")

except Exception as _ex:
    print("[INFO] ошибка с работой Postgresql", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] Подключение к Postgresql завершено")