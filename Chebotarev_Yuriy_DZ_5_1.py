"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...

"""


def odd_numgen(nums):
    set_oddnums = -1
    while set_oddnums <= nums:
        set_oddnums += 2
        yield set_oddnums


numb = odd_numgen(15)
print(next(numb))
print(next(numb))
print(next(numb))
print(next(numb))
print(next(numb))
