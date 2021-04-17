import requests
from decimal import *
from datetime import date


def currency_rates(currency):
    currency = currency.upper()
    req_link = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if currency not in req_link:
        return None

    rub = req_link[req_link.find('<Value>', req_link.find(currency)) + 7:req_link.find('</Value>', req_link.find(currency))]
    rub_dec = round(Decimal(rub.replace(',', '.')), 2)
    date_raw = req_link[req_link.find('Date="') + 6:req_link.find('"', req_link.find('Date="') + 6)].split('.')
    day, month, year = map(int, date_raw)
    date_t = date(day=day, month=month, year=year)

    return f'{currency}  {date_t}  {rub_dec}'


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('byn'))
