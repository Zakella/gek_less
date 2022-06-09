from itertools import zip_longest


# вариант 1
def timetable():
    for ind, tutor in enumerate(tutors):
        if ind + 1 > len(klasses):
            tupl = (tutor, None)
        else:
            tupl = (tutor, klasses[tutors.index(tutor)])
        yield tupl


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав', "Алексей", "Михаил"
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

result = timetable()
print(*result)

# вариант 2
result = ((tutor, None) if ind + 1 > len(klasses) else (tutor, klasses[tutors.index(tutor)]) for ind, tutor in enumerate(tutors))
print(*result)

#вариант 3
print(*{i for i in zip_longest(tutors, klasses)})

