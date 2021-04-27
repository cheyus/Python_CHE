import sys

sale = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as sale_file:
    sale_file.write(sale + '\n')
