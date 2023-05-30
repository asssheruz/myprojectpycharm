# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
#  повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые
#  нужно перевернуть
# """
# n = int(input('Введите число монеток: '))
# from random import randint
# a, b = 0, 0
# for i in range(n):
#     temp = randint(0, 1)
#     print(temp, end=' ')
#     if temp > 0: a += 1
#     else: b += 1
# print()
# if a > b:
#     print(f'Нужно перевернуть {b} монеток')
# else:
#     print(f'Нужно перевернуть {a} монеток')


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input('Введите сумму числа: '))
p = int(input('Введите произведение: '))
a = 0
for x in range(s):
    for y in range(s):
        if x + y == s and x * y == p:
            a += 1
            print(x, y)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
n = int(input('Введите число N: '))
k = 0
res = 1
while res < n+1:
    print(res, end=' ')
    k += 1
    res = 2 ** k