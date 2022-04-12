# вариант 1 без генератора
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

rezult = timetable()
print(*rezult)

# вариант 2
rezult = ((tutor, None) if ind + 1 > len(klasses) else (tutor, klasses[tutors.index(tutor)]) for ind, tutor in enumerate(tutors))
print(*rezult)