"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
 кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
"""

with open('nginx_logs.txt', 'r') as my_file:
    result = []
    for line in my_file:
        line_slp = line.split()
        result.append((line_slp[0], line_slp[5].replace('"', ''), line_slp[6]))
print(result)
