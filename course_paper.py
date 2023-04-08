from tkinter import *
from tkinter import ttk
import psycopg2

list_create_database = []
list_output_current_tables = []
list_deleting_a_table = []
list_existing_users = []
list_existing_product = []
list_deleting_a_value = []
list_editing_a_table = []

def windows():
    root = Tk()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x, y))
    root.geometry("504x300")
    root.title("Курсовая работа")

    '''Функция по созданию таблицы'''
    def create_database():
        windows_create_database = Toplevel(root)
        x = (windows_create_database.winfo_screenwidth() - windows_create_database.winfo_reqwidth()) / 2
        y = (windows_create_database.winfo_screenheight() - windows_create_database.winfo_reqheight()) / 2
        windows_create_database.wm_geometry("+%d+%d" % (x, y))
        windows_create_database.geometry("500x300")
        windows_create_database.title("Курсовая работа")

        '''Вывод информациия в массив и вызов создания таблицы в БД'''
        def bt_cr_db():
            name = entry_name_database.get()
            first_column = entry_creating_columns_one.get()
            second_column = entry_creating_columns_two.get()
            the_third_column = entry_creating_columns_three.get()
            fourth_column = entry_creating_columns_four.get()
            list_create_database.append(name)
            list_create_database.append(first_column)
            list_create_database.append(second_column)
            list_create_database.append(the_third_column)
            list_create_database.append(fourth_column)
            working_with_the_database.connecting_to_the_database(1)
            list_create_database.clear()
            entry_name_database.delete(0, END)
            entry_creating_columns_one.delete(0, END)
            entry_creating_columns_two.delete(0, END)
            entry_creating_columns_three.delete(0, END)
            entry_creating_columns_four.delete(0, END)

        '''Ввод наименовая таблицы'''
        name_database = Label(windows_create_database, text="Введите нименование БД")
        name_database.grid(column=0, row=1)

        entry_name_database = Entry(windows_create_database)
        entry_name_database.grid(column=1, row=1)

        '''Добавление в таблцу столбца №1'''
        creating_columns_one = Label(windows_create_database, text="Добавить в таблицу столбец №1 ")
        creating_columns_one.grid(column=0, row=2)

        entry_creating_columns_one = Entry(windows_create_database)
        entry_creating_columns_one.grid(column=1, row=2)

        '''Добавление в таблцу столбца №2'''
        creating_columns_two = Label(windows_create_database, text="Добавить в таблицу столбец №2 ")
        creating_columns_two.grid(column=0, row=3)

        entry_creating_columns_two = Entry(windows_create_database)
        entry_creating_columns_two.grid(column=1, row=3)

        '''Добавление в таблцу столбца №3'''
        creating_columns_three = Label(windows_create_database, text="Добавить в таблицу столбец №3 ")
        creating_columns_three.grid(column=0, row=4)

        entry_creating_columns_three = Entry(windows_create_database)
        entry_creating_columns_three.grid(column=1, row=4)

        '''Добавление в таблцу столбца №4'''
        creating_columns_four = Label(windows_create_database, text="Добавить в таблицу столбец №4 ")
        creating_columns_four.grid(column=0, row=5)

        entry_creating_columns_four = Entry(windows_create_database)
        entry_creating_columns_four.grid(column=1, row=5)

        bt_create_database = Button(windows_create_database, text="Создать таблицу", command=bt_cr_db)
        bt_create_database.grid(sticky=W, pady=50)

        go_back = Button(windows_create_database, text="Вернуться назад", command=windows_create_database.destroy)
        go_back.grid()

        windows_create_database.mainloop()
    
    '''Окно просмотра текущих таблиц'''
    def view_current_tables():
        windows_view_current_tables = Toplevel(root)
        x = (windows_view_current_tables.winfo_screenwidth() - windows_view_current_tables.winfo_reqwidth()) / 2
        y = (windows_view_current_tables.winfo_screenheight() - windows_view_current_tables.winfo_reqheight()) / 2
        windows_view_current_tables.wm_geometry("+%d+%d" % (x, y))
        windows_view_current_tables.geometry("600x300")
        windows_view_current_tables.title("Курсовая работа")
        working_with_the_database.connecting_to_the_database(2)

        colums = ("name", "type", "owner")
        tree = ttk.Treeview(windows_view_current_tables, columns=colums, show="headings")
        tree.grid()

        tree.heading('name', text="Наименование")
        tree.heading('type', text="Тип")
        tree.heading('owner', text="Владелей")

        for table in list_output_current_tables:
            tree.insert("", END, values=table)
        list_output_current_tables.clear()

        go_back = Button(windows_view_current_tables, text="Вернуться назад", command=windows_view_current_tables.destroy)
        go_back.grid(sticky=W)

        windows_view_current_tables.mainloop()

    '''Функция удаления таблицы'''
    def deleting_a_table():
        windows_deleting_a_table = Toplevel(root)
        x = (windows_deleting_a_table.winfo_screenwidth() - windows_deleting_a_table.winfo_reqwidth()) / 2
        y = (windows_deleting_a_table.winfo_screenheight() - windows_deleting_a_table.winfo_reqheight()) / 2
        windows_deleting_a_table.wm_geometry("+%d+%d" % (x, y))
        windows_deleting_a_table.geometry("600x300")
        windows_deleting_a_table.title("Курсовая работа")
        working_with_the_database.connecting_to_the_database(2)

        colums = ("name", "type", "owner")
        tree = ttk.Treeview(windows_deleting_a_table, columns=colums, show="headings")
        tree.grid()

        tree.heading('name', text="Наименование")
        tree.heading('type', text="Тип")
        tree.heading('owner', text="Владелей")

        for table in list_output_current_tables:
            tree.insert("", END, values=table)

        '''Взаимодействие с полозователем'''
        text_deleting_a_table = Label(windows_deleting_a_table, text='Напишите наименование таблицы')
        text_deleting_a_table.grid(column=0, row=1, sticky=W)

        entry_text_deleting_a_table = Entry(windows_deleting_a_table)
        entry_text_deleting_a_table.grid(column=0, row=1)

        '''Функция по удалению таблицы'''
        def cm_deleting_a_table():
            name = entry_text_deleting_a_table.get()
            list_deleting_a_table.append(name)
            working_with_the_database.connecting_to_the_database(3)
            list_deleting_a_table.clear()
            entry_text_deleting_a_table.delete(0, END)


        bt_deleting_a_table = Button(windows_deleting_a_table, text="Удалить", command=cm_deleting_a_table)
        bt_deleting_a_table.grid(row=1, sticky=W)
        
        go_back = Button(windows_deleting_a_table, text="Вернуться назад", command=windows_deleting_a_table.destroy)
        go_back.grid(row=2, sticky=W)

        windows_deleting_a_table.mainloop()

    '''Функция просмотра содержимого таблицы users'''
    def viewing_table_contents_def():
        windows_viewing_table_contents_def = Toplevel(root)
        x = (windows_viewing_table_contents_def.winfo_screenwidth() - windows_viewing_table_contents_def.winfo_reqwidth()) / 2
        y = (windows_viewing_table_contents_def.winfo_screenheight() - windows_viewing_table_contents_def.winfo_reqheight()) / 2
        windows_viewing_table_contents_def.wm_geometry("+%d+%d" % (x, y))
        windows_viewing_table_contents_def.geometry("970x300")
        windows_viewing_table_contents_def.title("Курсовая работа")
        working_with_the_database.connecting_to_the_database(4)

        colums = ('id', 'name', 'mail', 'post', 'phone')
        tree = ttk.Treeview(windows_viewing_table_contents_def, columns=colums, show="headings")
        tree.grid()

        '''Определение заголовков'''
        tree.heading("id", text='id')
        tree.heading("name", text="ФИО")
        tree.heading("mail", text="Электронная почта")
        tree.heading("post", text="Должность")
        tree.heading("phone", text="Номер телефона")

        for person in list_existing_users:
                tree.insert("", END, values=person)
        list_existing_users.clear()

        go_back = Button(windows_viewing_table_contents_def, text="Вернуться назад", command=windows_viewing_table_contents_def.destroy)
        go_back.grid(sticky=W)

        windows_viewing_table_contents_def.mainloop()
    
    '''Функция по редактированию таблицы'''
    def editing_a_table_def():
        windows_editing_a_table_def = Toplevel(root)
        x = (windows_editing_a_table_def.winfo_screenwidth() - windows_editing_a_table_def.winfo_reqwidth()) / 2
        y = (windows_editing_a_table_def.winfo_screenheight() - windows_editing_a_table_def.winfo_reqheight()) / 2
        windows_editing_a_table_def.wm_geometry("+%d+%d" % (x, y))
        windows_editing_a_table_def.geometry("970x400")
        windows_editing_a_table_def.title("Курсовая работа")
        working_with_the_database.connecting_to_the_database(4)

        def cm_editing_a_table():
            name_column = entry_text_editing_a_table.get()
            text_culumn_one =  entry_text_editing_a_table_column_one.get()
            text_culumn_two = entry_text_editing_a_table_column_two.get()
            list_editing_a_table.append(name_column)
            list_editing_a_table.append(text_culumn_one)
            list_editing_a_table.append(text_culumn_two)
            working_with_the_database.connecting_to_the_database(5)
            list_editing_a_table.clear()
            entry_text_editing_a_table.delete(0, END)
            entry_text_editing_a_table_column_one.delete(0, END)
            entry_text_editing_a_table_column_two.delete(0, END)

        colums = ('id', 'name', 'mail', 'post', 'phone')
        tree = ttk.Treeview(windows_editing_a_table_def, columns=colums, show="headings")
        tree.grid()

        '''Определение заголовков'''
        tree.heading("id", text='id')
        tree.heading("name", text="ФИО (nick_name)")
        tree.heading("mail", text="Электронная почта (mail_name)")
        tree.heading("post", text="Должность (post)")
        tree.heading("phone", text="Номер телефона (phone_number)")

        for person in list_existing_users:
                tree.insert("", END, values=person)
        list_existing_users.clear()

        '''Работа с пользователем'''
        '''Определения стобца'''
        text_editing_a_table = Label(windows_editing_a_table_def, text="Введи имя столбца")
        text_editing_a_table.grid(column=0, row=1, sticky=W)

        entry_text_editing_a_table = Entry(windows_editing_a_table_def)
        entry_text_editing_a_table.grid(column=0, row=1)

        '''Ввод что нужно изменить'''
        text_editing_a_table_column_one = Label(windows_editing_a_table_def, text="Введите что изменить")
        text_editing_a_table_column_one.grid(column=0, row=2, sticky=W)

        entry_text_editing_a_table_column_one = Entry(windows_editing_a_table_def)
        entry_text_editing_a_table_column_one.grid(column=0, row=2)

        '''Ввод на что изменить'''
        text_editing_a_table_column_two = Label(windows_editing_a_table_def, text="Введите на что изменить")
        text_editing_a_table_column_two.grid(column=0, row=3, sticky=W)

        entry_text_editing_a_table_column_two = Entry(windows_editing_a_table_def)
        entry_text_editing_a_table_column_two.grid(column=0, row=3)

        '''Кнопки'''
        bt_editing_a_table = Button(windows_editing_a_table_def, text="Изменить", command=cm_editing_a_table)
        bt_editing_a_table.grid(row=4, sticky=W)

        go_back = Button(windows_editing_a_table_def, text="Вернуться назад", command=windows_editing_a_table_def.destroy)
        go_back.grid(row=5, sticky=W)

        windows_editing_a_table_def.mainloop()

    '''Функция по удалению значения из таблицы'''
    def deleting_a_value_from_a_table_def():
        windows_deleting_a_value_from_a_table_def = Toplevel(root)
        x = (windows_deleting_a_value_from_a_table_def.winfo_screenwidth() - windows_deleting_a_value_from_a_table_def.winfo_reqwidth()) / 2
        y = (windows_deleting_a_value_from_a_table_def.winfo_screenheight() - windows_deleting_a_value_from_a_table_def.winfo_reqheight()) / 2
        windows_deleting_a_value_from_a_table_def.wm_geometry("+%d+%d" % (x, y))
        windows_deleting_a_value_from_a_table_def.geometry("1200x300")
        windows_deleting_a_value_from_a_table_def.title("Курсовая работа")
        working_with_the_database.connecting_to_the_database(6)

        '''Функция по удалению значения из таблицы'''
        def deleting_a_value():
            id_table = entry_text_deleting_a_value.get()
            list_deleting_a_value.append(id_table)
            working_with_the_database.connecting_to_the_database(7)
            list_deleting_a_value.clear()
            entry_text_deleting_a_value.delete(0, END)

        columns = ('id', 'name', 'classification', 'category', 'rating', 'price')

        tree = ttk.Treeview(windows_deleting_a_value_from_a_table_def, columns=columns, show="headings")
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
        list_existing_product.clear()

        '''Работа с пользователем'''
        text_deleting_a_value = Label(windows_deleting_a_value_from_a_table_def, text="Введи id товара")
        text_deleting_a_value.grid(column=0, row=1, sticky=W)

        entry_text_deleting_a_value = Entry(windows_deleting_a_value_from_a_table_def)
        entry_text_deleting_a_value.grid(column=0, row=1)

        '''Кнопка по удалению значения из таблицы'''
        bt_deleting_a_value = Button(windows_deleting_a_value_from_a_table_def, text="Удалить", command=deleting_a_value)
        bt_deleting_a_value.grid(row=2, sticky=W)

        '''Кнопка по возвращению'''
        go_back = Button(windows_deleting_a_value_from_a_table_def, text="Вернуться назад", command=windows_deleting_a_value_from_a_table_def.destroy)
        go_back.grid(row=3, sticky=W)

        windows_deleting_a_value_from_a_table_def.mainloop()

    text_info = "Приветстую вас на курсовой работа\n стундента - Евстюнин Александр Константинович\nгруппы -213-322"
    info_text = Label(root, text=text_info)
    info_text.grid(ipadx=110, ipady=50)

    creating_a_table_in_the_database = Button(root, text="Создать таблицу", command=create_database)
    creating_a_table_in_the_database.grid(column=0, row=1, sticky=W, ipadx=20)

    viewing_existing_tables = Button(root, text="Просмотр существующих таблиц", command=view_current_tables)
    viewing_existing_tables.grid(column=0, row=1, sticky=E)

    delete_a_table = Button(root, text="Удаление таблицы", command=deleting_a_table)
    delete_a_table.grid(column=0, row=2, sticky=W, ipadx=20)

    viewing_table_contents = Button(root, text="Посмотреть содержимое таблицы", command=viewing_table_contents_def)
    viewing_table_contents.grid(row=2, sticky=E)

    editing_a_table = Button(root, text="Редактирование таблицы", command=editing_a_table_def)
    editing_a_table.grid(column=0, row=3, sticky=W, ipadx=20)

    deleting_a_value_from_a_table = Button(root, text='Удаление значения из таблицы', command=deleting_a_value_from_a_table_def)
    deleting_a_value_from_a_table.grid(row=3, sticky=E)

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

            '''Обозначения переменных вызова функций
            1 - Создание таблицы
            2 - Вывод всех таблиц public
            3 - Удаление таблицы
            4 - просмотр содержисмого из таблицы users
            5 - редактирование значений в таблице users
            6 - Просмотр содержимого из таблицы product
            7 - Удаления значения из таблицы product'''
            if arg == 1:
                working_with_the_database.creating_a_table(connection, list_create_database[0], list_create_database[1], list_create_database[2], list_create_database[3], list_create_database[4])
            elif arg == 2:
                working_with_the_database.output_current_tables(connection)
            elif arg == 3:
                working_with_the_database.deleting_a_table(connection, list_deleting_a_table[0])
            elif arg == 4:
                working_with_the_database.viewing_table_contents(connection)
            elif arg == 5:
                working_with_the_database.readctation_editing_a_table(connection, list_editing_a_table[0], list_editing_a_table[1], list_editing_a_table[2])
            elif arg == 6:
                working_with_the_database.output_of_information_from_the_table(connection)
            elif arg == 7:
                working_with_the_database.deleting_id_table_product(connection)

        except Exception as _ex:
            print("[INFO] ошибка с работой Postgresql", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] Подключение к Postgresql завершено")

    '''Функция по созданию БД'''
    def creating_a_table(arg, name, first_column, second_column, the_third_column, fourth_column):
        with arg.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE {}(
                id serial PRIMARY KEY,
                {} varchar(80) NOT NULL,
                {} varchar(50) NOT NULL,
                {} varchar(50) NOT NULL,
                {} varchar(50) NOT NULL);""".format(name, first_column, second_column, the_third_column, fourth_column)
        )
        print("[INFO] Таблица успешно создана")

    '''Вывод информации по перечню таблиц'''
    def output_current_tables(arg):
        with arg.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM pg_catalog.pg_tables WHERE schemaname = 'public';"""
            )
            for person in cursor.fetchall():
                list_output_current_tables.append([person[1], person[0], person[2]])

    '''Функция по удалению таблиц'''
    def deleting_a_table(arg, name):
        with arg.cursor() as cursor:
            cursor.execute(
                """DROP TABLE {};""".format(name)
            )

    '''Функция по просмотра содержимого в таблице users'''
    def viewing_table_contents(arg):
        with arg.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM users"""
            )
            for person in cursor.fetchall():
                #print("{} - {} - {} - {}".format(person[1], person[2], person[3], person[4]))
                list_existing_users.append([person[0], person[1], person[2], person[3], person[4]])

    '''Функция по выводу товартов из таблицы product'''
    def output_of_information_from_the_table(arg):
        with arg.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM product"""
            )
            for person in cursor.fetchall():
                #print("{} - {} - {} - {}".format(person[1], person[2], person[3], person[4]))
                list_existing_product.append([person[0], person[1], person[2], person[3], person[4], person[5]])

    '''Функция по удалению значения из таблицы product'''
    def deleting_id_table_product(arg):
        with arg.cursor() as cursor:
            cursor.execute("""
            DELETE FROM product WHERE id='{}'
            """.format(list_deleting_a_value[0]))

    '''Функция по редактированию значений в таблице users'''
    def readctation_editing_a_table(arg, name_column, text_culumn_one, text_culumn_two):
        with arg.cursor() as cursor:
            cursor.execute("""
            UPDATE users SET {} = '{}' WHERE {} = '{}';
            """.format(name_column, text_culumn_two, name_column, text_culumn_one))

if __name__ == "__main__":
    windows()
    