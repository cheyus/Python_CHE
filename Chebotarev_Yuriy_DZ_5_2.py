"""
2*. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
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

*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""
import sys


def odd_numgen(nums):
    set_oddnums = (num for num in range(1, nums + 1, 2))
    return set_oddnums


numb = odd_numgen(10)
print(type(numb), sys.getsizeof(numb))
print(next(numb))
print(next(numb))
print(next(numb))
print(next(numb))
print(next(numb))
