# Скрипт формирования графика, его сохранения локально и в интернет-репозиторий api.imgbb.com

import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime
import matplotlib.ticker as ticker
import base64
import requests

PATH_TO_BD = '/root/Rit/main.db'
key = 'b8e0a42ff75159b0c5882635596627d3'
print('Script plot.py started!')

def get_data():
    with sqlite3.connect(PATH_TO_BD) as conn:
        cur = conn.cursor()
        cmd = 'SELECT * FROM likes'
        try:
            cur.execute(cmd)
            result = cur.fetchall()
            if result:
                return result
        except Exception as ex:
            print(ex)

def upload_foto(filename):
    with open(filename, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": key,
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)
        print(res)

x = []
y = []

result = get_data()
for item in result:
    x.append(item[2])
    y.append(item[1])

plt.plot(x, y)
plt.yticks([min(y), max(y)])
plt.xticks([min(x), max(x)])
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:}"))
plt.legend(['Лайки'])
plt.xlabel('Время')
plt.ylabel('Количество')
plt.title('График количества лайков во времени')
filename = '/root/Rit/pngs/likes_{}'.format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
plt.savefig(filename)
upload_foto('{}.png'.format(filename))

print('Script plot.py was finished!')
