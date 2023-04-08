from tkinter import *
from tkinter import ttk
import psycopg2

list_new_product = []
list_existing_product = []
list_sort_by_rating = []
list_view_cheap_products = []

class working_with_the_user:
    def windows():
        '''Функция по доавлению товра в БД'''
        def add_product():
            name = entry_name_product.get()
            classification = entry_product_classification.get()
            category = entry_age_category.get()
            rating = entry_rating_assessment.get()
            price = entry_product_price.get()
            list_new_product.append(name)
            list_new_product.append(classification)
            list_new_product.append(category)
            list_new_product.append(rating)
            list_new_product.append(price)
            working_with_the_database.connecting_to_the_database(2)
            list_new_product.clear()
            entry_name_product.delete(0, END)
            entry_product_classification.delete(0, END)
            entry_age_category.delete(0, END)
            entry_rating_assessment.delete(0, END)
            entry_product_price.delete(0, END)

        '''Просмотр товаров в таблице'''
        def table_of_products():
            '''Закрытие всех виджетов в стором окне'''
            working_with_the_database.connecting_to_the_database(3)
            info_text.destroy()
            name_product.destroy()
            entry_name_product.destroy()
            product_classification.destroy()
            entry_product_classification.destroy()
            age_category.destroy()
            entry_age_category.destroy()
            rating_assessment.destroy()
            entry_rating_assessment.destroy()
            product_price.destroy()
            entry_product_price.destroy()
            add_a_product_to_the_database.destroy()
            viewing_products.destroy()

            def expensive_items():
                '''Закрытие старых виджектов'''
                tree.destroy()
                the_most_expensive_products.destroy()
                working_with_the_database.connecting_to_the_database(4)
            
                def cheap_goods():
                    tree_two.destroy()
                    view_cheap_products.destroy()
                    working_with_the_database.connecting_to_the_database(5)

                    root.geometry("1200x300")
                    columns_three = ('id', 'name', 'classification', 'category', 'rating', 'price')

                    tree_three = ttk.Treeview(columns=columns_three, show="headings")
                    tree_three.grid()

                    '''Определение заголовков'''
                    tree_three.heading('id', text='id')
                    tree_three.heading('name', text='Наименования товара')
                    tree_three.heading('classification', text="Классификация товара")
                    tree_three.heading('category', text="Возрастная категирия")
                    tree_three.heading('rating', text="Рейтинговая оценка")
                    tree_three.heading('price', text="Цена")

                    for product in list_view_cheap_products:
                        tree_three.insert("", END, values=product)


                root.geometry("1200x300")
                columns_two = ('id', 'name', 'classification', 'category', 'rating', 'price')

                tree_two = ttk.Treeview(columns=columns_two, show="headings")
                tree_two.grid()

                '''Определение заголовков'''
                tree_two.heading('id', text='id')
                tree_two.heading('name', text='Наименования товара')
                tree_two.heading('classification', text="Классификация товара")
                tree_two.heading('category', text="Возрастная категирия")
                tree_two.heading('rating', text="Рейтинговая оценка")
                tree_two.heading('price', text="Цена")

                for product in list_sort_by_rating:
                    tree_two.insert("", END, values=product)

                view_cheap_products = Button(text="Просмотр дешовых товаров", command=cheap_goods)
                view_cheap_products.grid(sticky=W)


            '''Создание таблицы и вызов парсинга инфы из БД'''
            root.geometry('1200x300')
            columns = ('id', 'name', 'classification', 'category', 'rating', 'price')

            tree = ttk.Treeview(columns=columns, show="headings")
            tree.grid()

            '''Определение заголовков'''
            tree.heading('id', text='id')
            tree.heading('name', text='Наименования товара')
            tree.heading('classification', text="Классификация товара")
            tree.heading('category', text="Возрастная категирия")
            tree.heading('rating', text="Рейтинговая оценка")
            tree.heading('price', text="Цена")

            '''Добавление товара в таблицу'''
            for product in list_existing_product:
                tree.insert("", END, values=product)

            the_most_expensive_products = Button(text="Просмотр по рейтингу", command=expensive_items)
            the_most_expensive_products.grid(sticky=W)


        root = Tk()
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.wm_geometry("+%d+%d" % (x, y))
        root.geometry("500x300")
        root.title("Лабораторная работа №5")

        info_text = Label(text="Окно создания новых таваров")
        info_text.grid(column=0, row=0)

        '''Наименования товара'''
        name_product = Label(text="Наименование товара")
        name_product.grid(column=0, row=1)

        entry_name_product = Entry()
        entry_name_product.grid(column=1, row=1, ipadx=50)

        '''Классификация товара'''
        product_classification = Label(text="Классификация товара")
        product_classification.grid(column=0, row=2)

        entry_product_classification = Entry()
        entry_product_classification.grid(column=1, row=2, ipadx=50)

        '''Возрастная категория для товара'''
        age_category = Label(text="Возрастная катигория товара")
        age_category.grid(column=0, row=3)

        entry_age_category = Entry()
        entry_age_category.grid(column=1, row=3, ipadx=50)

        '''Рейтинговая оценка'''
        rating_assessment = Label(text="Рейтинговая оценка")
        rating_assessment.grid(column=0, row=4)

        entry_rating_assessment = Entry()
        entry_rating_assessment.grid(column=1, row=4, ipadx=50)

        '''Цена товара'''
        product_price = Label(text="Цена товара")
        product_price.grid(column=0, row=5)

        entry_product_price = Entry()
        entry_product_price.grid(column=1, row=5, ipadx=50)

        '''Кнопка по добавлению товара в БД'''
        add_a_product_to_the_database = Button(text="Добавить товар в БД", command=add_product)
        add_a_product_to_the_database.grid(sticky=W, pady=10)

        '''Кнопка просмотра товаров в БД'''
        viewing_products = Button(text="Посмотреть существующие товары", command=table_of_products)
        viewing_products.grid(sticky=W, pady=10)

        root.mainloop()

class working_with_the_database:
    '''Функция по подключению в БД'''
    def connecting_to_the_database(arg):
        try:
            connection = psycopg2.connect(
            host = "127.0.0.1",
            port = "5432",
            user = "postgres",
            password ="12345678",
            database = "db_base"
            )
            connection.autocommit = True
        
            '''Обозваничея вызова
            1 - создание БД
            2 - Добавление информации в таблцу
            3 - Вывод информации из таблицы
            4 - градация по порядку'''
            if arg == 1:
                working_with_the_database.creating_a_table(connection)
            elif arg == 2:
                working_with_the_database.add_product(connection, list_new_product[0], list_new_product[1], list_new_product[2], list_new_product[3], list_new_product[4])
            elif arg == 3:
                working_with_the_database.output_of_information_from_the_table(connection)
            elif arg == 4:
                working_with_the_database.output_of_information_from_the_table_rating(connection)
            elif arg == 5:
                working_with_the_database.output_of_information_from_the_table_cheap(connection)

        except Exception as _ex:
            print("[INFO] ошибка с работой Postgresql", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] Подключение к Postgresql завершено")

    '''Функция по созданию БД'''
    def creating_a_table(arg):
        with arg.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE product(
                id serial PRIMARY KEY,
                name_product varchar(80) NOT NULL,
                product_classification varchar(50) NOT NULL,
                age_category varchar(50) NOT NULL,
                rating_assessment varchar(50) NOT NULL,
                product_price varchar(50) NOT NULL);"""
        )
        print("[INFO] Таблица успешно создана") 

    '''Функция по добавлению товара в БД'''    
    def add_product(arg, name, classification, category, rating, price):
        with arg.cursor() as cursor:
            cursor.execute(
                """INSERT INTO product (name_product, product_classification, age_category, rating_assessment, product_price) VALUES
                ('{}', '{}', '{}', '{}', '{}')""".format(name, classification, category, rating, price))
            print("[INFO] Добавление информации в таблицу пройдено успешно")

    '''Вывод информации из таблицы product'''
    def output_of_information_from_the_table(arg):
        with arg.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM product"""
            )
            for person in cursor.fetchall():
                #print("{} - {} - {} - {}".format(person[1], person[2], person[3], person[4]))
                list_existing_product.append([person[0], person[1], person[2], person[3], person[4], person[5]])

    def output_of_information_from_the_table_rating(arg):
        with arg.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM product ORDER BY product_price"""
            )
            for person in cursor.fetchall():
                list_sort_by_rating.append([person[0], person[1], person[2], person[3], person[4], person[5]])

    def output_of_information_from_the_table_cheap(arg):
        with arg.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM product ORDER BY product_price limit 2"""
            )
            for person in cursor.fetchall():
                list_view_cheap_products.append([person[0], person[1], person[2], person[3], person[4], person[5]])

if __name__ == "__main__":
    working_with_the_database.connecting_to_the_database(1)
    working_with_the_user.windows()
