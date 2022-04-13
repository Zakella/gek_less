src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# вариант 1
repeat_list = set()
uniq_list = set()

for value in src:
    if value in repeat_list:
        continue
    else:
        if value in uniq_list:
            uniq_list.remove(value)
            repeat_list.add(value)
            continue
    uniq_list.add(value)

print(uniq_list)

# вариант 2
print([value for value in src if value in uniq_list])