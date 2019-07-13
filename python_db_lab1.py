'''
Пусть в таблице catalogs базы данных shop в строке name могут
находиться пустые строки и поля принимающие значение NULL.
Напишите запрос, который заменяет все такие поля на строку ‘empty’.
Помните, что на уроке мы установили уникальность на поле name.
Возможно ли оставить это условие? Почему?
'''
from urllib.request import Request, urlopen
import requests
import gzip
import re
import datetime

current_date = datetime.date.today()

s = ['Видеокарта', 'Материнская плата', 'Процессор']

for idx, val in enumerate(s):
    print(idx, val)
    response = requests.post('http://localhost:8040/tarantool_dummies',
                              json={"method": "insert_catalogs", "params": [{'name': val}]})
    if response.status_code != 200:
        print("Сервер БД недоступен")
    else:
        print(response.json())


response = requests.post('http://localhost:8040/tarantool_dummies',
                          json={"method": "select_catalogs", "params": []})

print(response.json())