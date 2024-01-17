from random import randint

num = [randint(-10, 10) for _ in range(5)]
print(num)

print("Сумма отрицательных чисел", sum(i for i in num if i < 0))
print("Сумма четных чисел;", sum(i for i in num if i%2 == 0))
print("Сумма нечетных чисел;", sum(i for i in num if i%2 != 0))
lol = 1
for i in num:
    if i %3 == 0:
        lol = 1

print("Произведение элементов с индексами кратными 3;", lol)
min = num.index(min(num))
max = num.index(max(num))
if min < max:
    min_max = 1
    for i in range(min +1, max):
        min_max *= num[i]
else:
    min_max = 1
    for i in range(max + 1, min):
        min_max *= num[i]
print("Произведение элементов между минимальным и максимальным элементом;", min_max)

s1 = s2 = 0
for s1, a in enumerate(num):
    if a > 0:
        break
for s2, a in enumerate(reversed(num)):
    if a > 0:
        break
s = sum(num[s1+1: -s2-1])
print("Сумму элементов, находящихся между первым и последним положительными элементами.", s)