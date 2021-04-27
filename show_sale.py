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
