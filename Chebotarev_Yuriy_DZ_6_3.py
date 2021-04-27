"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно, что при хранении
данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби  (hobby.csv):
скалолазание,охота
горные лыжи

"""
from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as my_file_u:
    users = []
    for line in my_file_u:
        user = line.replace(',', ' ').replace('\n', '')
        users.append(user)

with open('hobby.csv', 'r', encoding='utf-8') as my_file_h:
    hobbies = []
    for line in my_file_h:
        hobby = line.replace('\n', '')
        hobbies.append(hobby)

if len(users) < len(hobbies):
    exit(1)

out_dic = {}
for user, hobby in zip_longest(users, hobbies):
    out_dic[user] = hobby

with open('TaskDZ_3.json', 'w', encoding='utf-8') as out_file:
    json.dump(out_dic, out_file, ensure_ascii=False)

print(out_dic)