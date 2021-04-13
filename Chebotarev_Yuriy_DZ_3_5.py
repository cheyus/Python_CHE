"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
(по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(joke_num, repetition=True):
    """
    :param joke_num: the number of required number of jokes is set
    :param repetition: allow repetition of words in jokes
    :return: list of required number of jokes
    """
    jokes = []
    for i in range(joke_num):
        raw_joke = []
        if repetition:
            raw_joke.append(random.choice(nouns))
            raw_joke.append(random.choice(adverbs))
            raw_joke.append(random.choice(adjectives))
        else:
            raw_joke.append(nouns.pop(random.randrange(len(nouns))))
            raw_joke.append(adverbs.pop(random.randrange(len(adverbs))))
            raw_joke.append(adjectives.pop(random.randrange(len(adjectives))))
        joke = ' '.join(raw_joke)
        jokes.append(joke)
    return jokes


print(get_jokes(3, False))
