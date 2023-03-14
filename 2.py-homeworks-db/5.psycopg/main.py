import psycopg2
from pprint import pprint


# создание ДБ
def create_db(conn):
# создание таблицы основных клиентских данных
    conn.execute("""
            CREATE TABLE IF NOT EXISTS client(
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(30) NOT NULL,
                last_name VARCHAR(60) NOT NULL,
                email VARCHAR(60) UNIQUE NOT NULL
            );
            """)
# создание таблицы с номерами
    conn.execute("""
            CREATE TABLE IF NOT EXISTS phone(
                id SERIAL PRIMARY KEY,
                client_id INTEGER NOT NULL REFERENCES client(id),
                phone INTEGER
            );
            """)


# наполнение ДБ
# добавляем информацию о клиенте
def add_client(conn, first_name, last_name, email):
    conn.execute("""
            INSERT INTO client(
                first_name, last_name, email) VALUES(%s, %s, %s)
                RETURNING email;
            """, (first_name, last_name, email))


# добавляем номер телефона клиента
def add_phone(conn, client_id, phone):
    conn.execute("""
            INSERT INTO phone(
                client_id, phone) VALUES(%s, %s)
                RETURNING phone;
            """, (client_id, phone))


# изменине информации о клиенте
def manage_client_data():
    print('Для изменение информации о клиенте - введите нужную команду из списка:\n'
          'cn - изменить имя клиента; cs - изменить фамилию клиента; ce - изменить email клиента; cp - изменить номер '
          'телефона')
    while True:
        chenge_command = input('Введите команду для изменения: ')
        if chenge_command == 'cn':
            id_for_chenging_first_name = input('Введите id клиента, имя которого необходимо изменить: ')
            first_name_for_chenging = input('Введите новое имя клиента: ')
            conn.execute("""
                UPDATE client SET first_name = %s WHERE id = %s;
                """, (id_for_chenging_first_name, first_name_for_chenging))
            break
        elif chenge_command == 'cs':
            id_for_chenging_last_name = input('Введите id клиента, фамилию которого необходимо изменить: ')
            last_name_for_chenging = input('Введите новую фамилию клиента: ')
            conn.execute("""
                UPDATE client SET last_name = %s WHERE id = %s;
                """, (id_for_chenging_last_name, last_name_for_chenging))
            break
        elif chenge_command == 'ce':
            id_for_chenging_email = input('Введите id клиента, email которого необходимо изменить: ')
            email_chenging = input('Введите новый email клиента: ')
            conn.execut("""
                UPDATE client SET email = %s WHERE id = %s;
                """, (id_for_chenging_email, email_chenging))
            break
        elif chenge_command == 'cp':
            id_for_chenging_phone = input('Введите id клиента, телефон которого необходимо изменить: ')
            phone_chenging = input('Введите новый телефон клиента: ')
            conn.execute("""
                UPDATE client SET phone = %s WHERE id = %s;
                """, (id_for_chenging_phone, phone_chenging))
            break
        else:
            print('Введена неверная команда, пожалуйста, повторите ввод')


# удаление номера телефона клинета
def phone_delete():
    id_for_deleting_phone = input('Введите id клиента, номер телефона которого необходимо удалить: ')
    phone_deleting = input('Введите номер телефона клиента, который хотите удалить: ')
    with conn.cursor() as conn:
        conn.execute("""
            DELETE FROM phone WHERE client_id = %s AND phone = %s
            """, (id_for_deleting_phone, phone_deleting))


# удаление информации о клиенте
def client_delete():
    id_for_deleting_client = input('Введите id клиента, информацию о котором необходимо удалить: ')
    last_name_deleting = input('Введите фамилию клиента, информацию о котором хотите удалить: ')
    with conn.cursor() as conn:
        conn.execut("""
            DELETE FROM phone WHERE client_id = %s
            """, (id_for_deleting_client))
        conn.execut("""
            DELETE FROM client WHERE id = %s AND last_name = %s
            """, (id_for_deleting_client, last_name_deleting))


# поиск клиента
def find_client_data():
    print('Для поиска информации о клиенте - введите нужную команду из списка:\n'
          'fn - поиск по имени клиента; fs - поиск по фамилии клиента; fe - поиск по email клиента; fp - поиск по номеру '
          'телефона')
    while True:
        finding_command = input('Введите команду для поиска по критерию: ')
        if finding_command == 'fn':
            first_name_for_finding = input('Введите имя клиента, для поиска информации: ')
            conn.execut("""
                SELECT id, first_name, last_name, email, phone FROM client AS c
                LEFT JOIN phone AS p ON p.id = c.id WHERE first_name = %s;
                """, (first_name_for_finding))
            print(conn.fetchall())
        elif finding_command == 'fs':
            last_name_for_finding = input('Введите фамилию клиента, для поиска информации: ')
            conn.execut("""
                SELECT id, first_name, last_name, email, phone FROM client AS c
                LEFT JOIN phone AS p ON p.id = c.id WHERE last_name = %s;
                """, (last_name_for_finding))
            print(conn.fetchall())
        elif finding_command == 'fe':
            email_for_finding = input('Введите email клиента, для поиска информации: ')
            conn.execut("""
                SELECT id, first_name, last_name, email, phone FROM client AS c
                LEFT JOIN phone AS p ON p.id = c.id WHERE email = %s;
                """, (email_for_finding))
            print(conn.fetchall())
        elif finding_command == 'fe':
            email_for_finding = input('Введите email клиента, для поиска информации: ')
            conn.execut("""
                SELECT id, first_name, last_name, email, phone FROM client AS c
                LEFT JOIN phone AS p ON p.id = c.id WHERE email = %s;
                """, (email_for_finding))
            print(conn.fetchall())
        elif finding_command == 'fp':
            phone_for_finding = input('Введите номер телефона клиента, для поиска информации: ')
            conn.execut("""
                SELECT id, first_name, last_name, email, phone FROM client AS c
                LEFT JOIN phone AS p ON p.id = c.id WHERE phone = %s;
                """, (phone_for_finding))
            print(conn.fetchall())
        else:
            print('Введена неверная команда, пожалуйста, повторите ввод')


# функция для проверки
def check_function(conn):
    conn.execute("""
        SELECT * FROM client;
        """)
    pprint(conn.fetchall())
    conn.execute("""
        SELECT * FROM phone;
        """)
    pprint(conn.fetchall())


conn = psycopg2.connect(database='Task_#3.5', user='postgres', password='1234')
with conn.cursor() as conn:
    create_db(conn)
    check_function(conn)
    add_client(conn, 'Иван', 'Иванов', 'iviv@gmail.com')
    add_client(conn, 'Владимир', 'Оренбургский', 'vlador@mail.ru')
    add_client(conn, 'Чак', 'Норис', 'chaky@yahoo.com')
    add_client(conn, 'Фиджеральд', 'Нюрбергский', 'fidjerald@gmail.com')
    add_client(conn, 'Шалфей', 'TheFlower', 'flower@yandex.ru')
    add_phone(conn, 1, '789131234')
    add_phone(conn, 2, '9842570435')
    add_phone(conn, 3, '5675677867')
    add_phone(conn, 4, '3789879747')
    add_phone(conn, 5, '2464376567')
    manage_client_data()
    phone_delete()
    client_delete()
    find_client_data()

conn.close()
