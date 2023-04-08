import psycopg2

def create_tables():
    '''Создание прервой таблицы пользователи - users'''
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE users(
            id serial PRIMARY KEY,
            name_mail varchar(100) NOT NULL,
            first_name varchar(50) NOT NULL,
            nick_name varchar(100) NOT NULL);""")
    print("[INFO] Таблица c пользователями успешно создана")

    '''Создание второй таблицы перечнем кино - list_of_films'''
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE list_of_films(
            id serial PRIMARY KEY,
            duration_of_the_film varchar(100) NOT NULL,
            first_name varchar(50) NOT NULL,
            nick_name varchar(100) NOT NULL);""")
    print("[INFO] Таблица c перечнем кино успешно создана")

    '''Создание третьей таблицы стоимости подписки - subscription_price'''
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE subscription_price(
            id serial PRIMARY KEY,
            price_list varchar(100) NOT NULL,
            first_name varchar(50) NOT NULL,
            nick_name varchar(100) NOT NULL);""")
    print("[INFO] Таблица c перечнем подписки успешно создана")

    '''Создание четвертая таблицы жанров кино - genres_of_cinema'''
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE genres_of_cinema(
            id serial PRIMARY KEY,
            horrors_list varchar(100) NOT NULL,
            comedy_name varchar(50) NOT NULL,
            nick_name varchar(100) NOT NULL);""")
    print("[INFO] Таблица c жанром кино успешно создана")

    '''Создание пятая таблицы рекоминдации - recommendations'''
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE recommendations(
            id serial PRIMARY KEY,
            first_place varchar(100) NOT NULL,
            second_place varchar(50) NOT NULL,
            nick_name varchar(100) NOT NULL);""")
    print("[INFO] Таблица c рекоминдациями кино успешно создана")

def filling_in_the_table():
    '''Заполнение прервой таблицы пользователи - users'''
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (nick_name, first_name, name_mail) VALUES
            ('Alex', 'politex', 'alex@mail.ru'),
            ('Vera', 'politex', 'vera@gmail.com'),
            ('Anna', 'politex', 'anna@yandex.ru')"""
        )
        print("[INFO] Добавление информации в таблицу users пройдено успешно")

    '''Заполнение второй таблицы перечьня фильмов - list_of_films'''
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO list_of_films (nick_name, first_name, duration_of_the_film) VALUES
            ('Star Wars 1', 'kino', 'two hours'),
            ('Star Wars 2', 'kino', 'two hours and 10 minutes'),
            ('Star Wars 3', 'kino', 'one hour')"""
        )
        print("[INFO] Добавление информации в таблицу list_of_films пройдено успешно")

    '''Заполнение третьей таблицы подписки - subscription_price'''
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO subscription_price (nick_name, first_name, price_list) VALUES
            ('full', 'bay', '500$'),
            ('average', 'bay', '350$'),
            ('children', 'bay', '150$')"""
        )
        print("[INFO] Добавление информации в таблицу subscription_price пройдено успешно")

    '''Заполнение цетвертой таблицы жанров кино - genres_of_cinema'''
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO genres_of_cinema (nick_name, comedy_name, horrors_list) VALUES
            ('Star Wars 1', '+', '-'),
            ('Star Wars 2', '-', '+'),
            ('Star Wars 3', '+', '-')"""
        )
        print("[INFO] Добавление информации в таблицу genres_of_cinema пройдено успешно")

    '''Заполнение пятой таблицы рекоминдации - recommendations'''
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO recommendations (nick_name, first_place, second_place) VALUES
            ('Star Wars 1', '+', '-'),
            ('Star Wars 2', '-', '+'),
            ('Star Wars 3', '+', '-')"""
        )
        print("[INFO] Добавление информации в таблицу recommendations пройдено успешно")

def multi_table_query():
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM users; 
            """
        )
    print(cursor.fetchone())

try:
    '''Подключение БД к postgresql'''
    connection = psycopg2.connect(
    host = "127.0.0.1",
    port = "8090",
    user = "postgres",
    password ="postgres",
    database = "postgres"
    )
    connection.autocommit = True

    #create_tables()
    #filling_in_the_table()
    multi_table_query()

except Exception as _ex:
    print("[INFO] ошибка с работой Postgresql", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] Подключение к Postgresql завершено")