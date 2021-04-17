"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal?
 Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
 вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
 В качестве примера выведите курсы доллара и евро.
 *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
 которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
 Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
Фрагмент xml:
<Valute ID="R01235">
<NumCode>840</NumCode>
<CharCode>USD</CharCode>
<Nominal>1</Nominal>
<Name>Доллар США</Name>
<Value>75,5535</Value>
</Valute>
"""

import requests
from decimal import *
from datetime import date


def currency_rates(currency):
    currency = currency.upper()
    req_link = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if currency not in req_link:
        return None

    rub = req_link[req_link.find('<Value>', req_link.find(currency)) + 7:req_link.find('</Value>', req_link.find(currency))]
    rub_dec = Decimal(rub.replace(',', '.'))
    date_raw = req_link[req_link.find('Date="') + 6:req_link.find('"', req_link.find('Date="') + 6)].split('.')
    day, month, year = map(int, date_raw)
    date_t = date(day=day, month=month, year=year)

    return f'{currency} {rub_dec} {date_t} {type(date_t)}'


print(currency_rates('usd'))
print(currency_rates('EUR'))
print(currency_rates('gbp'))
print(currency_rates('gbr'))

