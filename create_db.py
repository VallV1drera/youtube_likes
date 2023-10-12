# Утилита для управления базой
# Внимание! Функция clear_table не обнуляет счётчик id

import sqlite3

PATH_TO_BD = 'main.db'

def create_table():
    with sqlite3.connect(PATH_TO_BD) as conn:
        cur = conn.cursor()
        cmd = "CREATE TABLE likes (id INTEGER PRIMARY KEY AUTOINCREMENT, count INTEGER, time TIMESTAMP DEFAULT (datetime('now','localtime')))"
        try:
            cur.execute(cmd)
            print('Table created')
            conn.commit()
        except Exception as ex:
            print(ex)

def delete_table():
    with sqlite3.connect(PATH_TO_BD) as conn:
        cur = conn.cursor()
        cmd = 'DROP TABLE likes'
        try:
            cur.execute(cmd)
            print('Table deleted')
            conn.commit()
        except Exception as ex:
            print(ex)

def test_input():
    with sqlite3.connect(PATH_TO_BD) as conn:
        cur = conn.cursor()
        cmd = 'INSERT INTO likes (count) VALUES (1488)'
        try:
            cur.execute(cmd)
            print('Test input success')
            conn.commit()
        except Exception as ex:
            print(ex)

def test_output():
    with sqlite3.connect(PATH_TO_BD) as conn:
        cur = conn.cursor()
        cmd = 'SELECT * FROM likes'
        try:
            cur.execute(cmd)
            result = cur.fetchall()
            if result:
                print(result)
        except Exception as ex:
            print(ex)

def clear_table():
    with sqlite3.connect(PATH_TO_BD) as conn:
        cur = conn.cursor()
        cmd = 'DELETE FROM likes'
        try:
            cur.execute(cmd)
            print('Table cleared')
            conn.commit()
        except Exception as ex:
            print(ex)

menu = {1: create_table, 2: delete_table, 3: test_input, 4: test_output, 5: clear_table}
while True:
    for point in menu:
        print('{}: {}'.format(point, menu.get(point).__name__))
    choice = int(input('Enter 1-5: '))
    if choice:
        menu[choice]()
        input('Enter to continue')
