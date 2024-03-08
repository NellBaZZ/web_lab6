import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('postCurse.sqlite')
cursor = conn.cursor()

# 111111111111111111111111111
# Выберем клиентов и их покупки на определенный тип публикации с сортировкой по имени клиента:
query_1_1 = '''
SELECT c.FIO, c.address, p.name, d.name
FROM client c
JOIN purchase pu ON c.id = pu.id_client
JOIN publication p ON pu.id_publication = p.id
JOIN delivery d ON pu.id_delivery = d.id
WHERE p.id_type = 3
ORDER BY c.FIO;
'''
#выборка клиентов, у которых есть покупки с доставкой яндекс:
query_1_2 = '''
SELECT DISTINCT c.FIO, c.address, d.name
FROM client c
JOIN purchase pu ON c.id = pu.id_client
JOIN delivery d ON pu.id_delivery = d.id
WHERE d.name = 'yandex';
'''


# 22222222222222222222222222
# Количество покупок для каждого клиента:
query_2_1 = '''
SELECT c.FIO, COUNT(pu.id) AS num_purchases
FROM client c
LEFT JOIN purchase pu ON c.id = pu.id_client
GROUP BY c.id;
'''
# Средняя цена публикации для каждого типа:
query_2_2 = '''
SELECT tp.tip, AVG(p.price) AS average_price
FROM type_publication tp
JOIN publication p ON tp.id = p.id_type
GROUP BY tp.tip;
'''

# 333333333333333333333333
# Клиенты с наибольшим числом подписок:
query_3_1 = '''
SELECT c.FIO, c.address, COUNT(pu.id) AS num_purchases
FROM client c
JOIN purchase pu ON c.id = pu.id_client
GROUP BY c.id
ORDER BY num_purchases DESC
LIMIT 5;
'''
# Публикации, цены которых выше средней цены по типу:
query_3_2 = '''
SELECT p.name, p.price, tp.tip
FROM publication p
JOIN type_publication tp ON p.id_type = tp.id
WHERE p.price > (SELECT AVG(price) FROM publication WHERE id_type = p.id_type);

'''

## 444444444444444444444444
# Запрос с обновлением данных
query_4_1 = '''
UPDATE publication
SET price = price * 1.5
WHERE id_type = (SELECT id FROM type_publication WHERE tip = 'Газета');
'''
# Запрос с добавлением данных
query_4_2 = '''
INSERT INTO type_publication (tip) VALUES ('Электроннаяы книга');
'''
# Запрос с удалением данных
query_4_3 = '''
DELETE FROM courier WHERE FIO = 'Михайлов Михаил Михайлович';
'''


# Выполнение запросов
cursor.execute(query_1_1)
print('1.1 - ',cursor.fetchall())
cursor.execute(query_1_2)
print('1.2 - ',cursor.fetchall())

cursor.execute(query_2_1)
print('2.1 - ',cursor.fetchall())
cursor.execute(query_2_2)
print('2.2 - ',cursor.fetchall())

cursor.execute(query_3_1)
print('3.1 - ',cursor.fetchall())
cursor.execute(query_3_2)
print('3.2 - ',cursor.fetchall())

cursor.execute(query_4_1)
cursor.execute(query_4_2)
cursor.execute(query_4_3)
# Закрытие соединения с базой данных
conn.commit()
conn.close()