
# первый вариант
def nums_gen(max):
    for num in range(1, max, 2):
        yield num


print(*nums_gen(10**5))

# второй вариант
nums = (num for num in range(1, 100000, 2))
print(*nums)