"""
Реализовать простую систему хранения данных о суммах продаж булочной.
Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
При записи передавать из командной строки значение суммы продаж.
Для чтения данных реализовать в командной строке следующую логику:
просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
Примеры запуска скриптов:
python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
"""

import sys

sale = sys.argv[1]
with open('bakery.csv', 'w', encoding='utf-8') as sale_file:
    sale_file.write(sale + '\n')



with open('bakery.csv', 'r', encoding='utf-8') as sale_file:
    # print(f'строк в файле: {sum(1 for line in sale_file)}\n')
    for line in sale_file:
        print(line.replace('\n', ''))


import sys

sale = sys.argv[1:]
with open('bakery.csv', 'r', encoding='utf-8') as sale_file:
    if len(sale) == 0:
        for line in sale_file:
            print(line.strip())
    elif len(sale) > 1:
        start_idx = int(sale[0])
        end_idx = int(sale[1])
    else:
        start_idx = int(sale[0])
        end_idx = sum(1 for line in sale_file)
        sale_file.seek(0)

    for idx, line in enumerate(sale_file):
        if start_idx <= idx + 1 <= end_idx:
            print(line.replace('\n', ''))