import sqlite3

conn = sqlite3.connect('postCurse.sqlite')


# Ваш SQL-код для создания таблиц
conn.executescript('''

DROP TABLE IF EXISTS client;
CREATE TABLE client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL
);
PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS type_publication;
CREATE TABLE type_publication (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tip VARCHAR(30) NOT NULL UNIQUE
);

DROP TABLE IF EXISTS publication;
CREATE TABLE publication (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_type INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL UNIQUE,
    price INTEGER NOT NULL,
    FOREIGN KEY (id_type) REFERENCES type_publication(id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS purchase;
CREATE TABLE purchase (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_publication INTEGER NOT NULL,
    id_client INTEGER NOT NULL,
    id_delivery INTEGER NOT NULL,
    FOREIGN KEY (id_publication) REFERENCES publication(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_client) REFERENCES Client(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_delivery) REFERENCES delivery(id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS courier;
CREATE TABLE courier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    FIO VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS delivery;
CREATE TABLE delivery (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_courier INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_courier) REFERENCES courier(id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS review;
CREATE TABLE review (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER NOT NULL,
    id_delivery INTEGER NOT NULL,
    grade INTEGER NOT NULL,
    text VARCHAR(255),
    FOREIGN KEY (id_client) REFERENCES client(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_delivery) REFERENCES delivery(id) ON DELETE CASCADE ON UPDATE cascade
);
    ''')


cursor = conn.cursor()

cursor.execute("INSERT INTO courier (FIO) VALUES "
    "('Иванов Иван Иванович'), "
    "('Петров Петр Петрович'), "
    "('Сидоров Сидор Сидорович'), "
    "('Кузнецов Кузьма Кузьмич'), "
    "('Нельбасов Денис Манасович'), "     
    "('Копоть Максим Пиратович'), "
    "('Михайлов Пират Ананасович'), "           
    "('Михайлов Михаил Михайлович');")

cursor.execute("INSERT INTO client (id, fio, address) VALUES "
                   "('1', 'Нельбасов Денис Манасович', 'ул. Чернышевского д. 41 кв. 55'), "
                   "('2', 'Владимиров Владимир Владимирович', 'ул. Уланова д. 5 кв. 1'), "
                   "('3', 'Кошевой Олег Олегович', 'ул. Якутова д. 3 кв. 123'), "
                   "('4', 'Александров Александр Александрович', 'ул. Дом д. 2 кв. 4'), "
                   "('5', 'Давыдов Денис Денисович', 'ул. Котова д. 5 кв. 2'), "
                   "('6', 'Джугашвили Сталин Виссарионович', 'ул. Советская д. 123 кв. 3'), "
                   "('7', 'Нельбов Нельба Нельбович', 'ул. Нельбова д. 12 кв. 66'), "
                   "('8', 'Хотянов Хотик Хотикович', 'ул. Пушкинская д. 76 кв. 123'), "
                   "('9', 'Ленинов Совет Россиевич', 'ул. Советов д. 5 кв. 45'), "
                   "('10', 'Россиев Россия Россиевич', 'ул. Ветеранов д. 4 кв. 443'), "
                   "('11', 'Танков Танк Танкобоевич', 'ул. Ветеранов д. 3 кв. 666'), "
                   "('12', 'Романов Роман Романович', 'ул. Москова д. 2 кв. 123');")

cursor.execute("INSERT INTO type_publication (tip) VALUES "
                   "('Газета'), "
                   "('Журнал'), "
                   "('Журнал для взрослых'), "
                   "('Энциклопедия'), "
                   "('Учебник'), "
                   "('Книга'), "
                   "('Художественная литература');")

cursor.execute("INSERT INTO publication (id_type, name, price) VALUES "
                   "('1', 'fisher', '100'), "
                   "('2', 'hunter', '150'), "
                   "('4', 'Ипотека', '99999'), "
                   "('5', 'Охотник', '144'), "
                   "('6', 'Война', '100'), "
                   "('6', 'Мир', '100'), "
                   "('7', 'Война и Мир', '500'), "
                   "('1', 'Mortal', '300'), "
                   "('2', 'combat', '333'), "
                   "('3', 'Детский сад', '999'), "
                   "('4', 'dota', '155'), "
                   "('5', 'war thunder', '666'), "
                   "('6', 'Дюймовочка', '50'), "
                   "('7', 'Гарри Поттер', '1000');")

cursor.execute("INSERT INTO delivery (id_courier, name) VALUES "
               "('1', 'yandex'), "
               "('2', 'yandex'), "
               "('3', 'club'), "
               "('4', 'club'), "
               "('5', 'samokat'), "
               "('6', 'yandex'), "
               "('7', 'club'), "
               "('8', 'yandex');")

cursor.execute("INSERT INTO purchase (id_publication, id_client, id_delivery) VALUES "
               "('1', '1', '1'), "
               "('10', '2', '2'), "
               "('3', '3', '3'), "
               "('4', '4', '4'), "
               "('4', '8', '4'), "
               "('5', '8', '6'), "
               "('8', '7', '5'), "
               "('7', '10', '3'), "
               "('10', '11', '2'), "
               "('11', '5', '1'), "
               "('13', '5', '8'), "
               "('10', '5', '8');")

cursor.execute("INSERT INTO review (id_client, id_delivery, grade, text) VALUES "
               "('8', '4', '4',''), "
               "('8', '6', '5',''), "
               "('11', '2', '2',''), "
               "('1', '1', '1','Ужасно! Заказ потеряли и никак не отреагировали'), "
               "('2', '2', '2','Не понравилось, опоздали и заказ был испорчен'), "
               "('3', '3', '3','Средний сервис, можно лучше'), "
               "('4', '4', '4','Хорошая работа, но немного задержались'), "
               "('5', '5', '5','Отличный сервис, всегда все вовремя');")
conn.commit()
conn.close()