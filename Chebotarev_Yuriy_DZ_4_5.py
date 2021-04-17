import sys
import utils

# print(utils.currency_rates(sys.argv[1]))

try:
    cur = sys.argv[1]
except IndexError:
    print('Ошибка выполнения!')
else:
    print(utils.currency_rates(cur))
