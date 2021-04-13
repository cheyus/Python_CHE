"""*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
"""

dic_dz = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(dic_obj):
    if dic_dz.get(dic_obj.lower()) is None:
        translate = 'None'
    else:
        if dic_obj[0].istitle():
            translate = dic_dz.get(dic_obj.lower()).title()
        else:
            translate = dic_dz.get(dic_obj.lower())
    return translate


print(num_translate_adv('one'))
print(num_translate_adv('EighT'))
print(num_translate_adv('Test'))

