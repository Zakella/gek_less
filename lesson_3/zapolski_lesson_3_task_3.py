import random

def get_jokes(n):
    l1 = random.sample(nouns, n)
    l2 = random.sample(adverbs, n)
    l3 = random.sample(adjectives, n)
    list_4 = list(zip(l1, l2,l3))
    list_final = []
    for el in list_4:
        lis = list(el)
        list_final.append(" ".join(lis))
    return list_final

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(2))
