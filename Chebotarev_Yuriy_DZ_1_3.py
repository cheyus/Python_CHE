"""Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
Вывести все склонения для проверки.
"""

numbers = range(100)
for numb in numbers:
    if numb < 20:
        if numb == 1:
            print(numb, 'процент')
        elif 2 <= numb <= 4:
            print(numb, 'процента')
        else:
            print(numb, 'процентов')
    else:
        numb_check = numb % 10
        if numb_check == 1:
            print(numb, 'процент')
        elif 2 <= numb_check <= 4:
            print(numb, 'процента')
        else:
            print(numb, 'процентов')




