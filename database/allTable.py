import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('postCurse.sqlite')
cursor = conn.cursor()

# Получение списка таблиц в базе данных
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Вывод данных из каждой таблицы с подписанными столбцами
for table in tables:
    table_name = table[0]
    print(f"Таблица: {table_name}")

    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()

    column_names = [column[1] for column in columns]
    print(" | ".join(column_names))

    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()

    for row in rows:
        print(" | ".join([str(value) for value in row]))

    print("\n")

# Закрытие соединения с базой данных
conn.commit()
conn.close()