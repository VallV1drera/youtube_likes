# Скрипт сбора информации с API YouTube

import requests
import time
import sqlite3

PATH_TO_BD = '/root/Rit/main.db'
video_id = "dQw4w9WgXcQ&t"
api_key = "AIzaSyCCucwVt189YPj-nLVPT3PChAcoANmjjoI"

print('Запуск скрипта data_collector')

def input_data(data):
    with sqlite3.connect(PATH_TO_BD) as conn:
        cur = conn.cursor()
        cmd = 'INSERT INTO likes (count) VALUES ({})'.format(data)
        try:
            cur.execute(cmd)
            print('Input success')
            conn.commit()
        except Exception as ex:
            print(ex)

# Построить URL запроса
url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        like_count = data["items"][0]["statistics"]["likeCount"]
        input_data(like_count)
        time.sleep(300)
    else:
        print("Ошибка при получении количества лайков")
        exit(1)
