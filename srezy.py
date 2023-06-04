# a = 'Hello world'
# b = [1,2,3,4,5,6,7,8]
# print(a[::-2])
# # print(b[3000])
# print(list(a))
# print(a.split())

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
#
# 22:22
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# str = input("Введите любое слово или предложение: ").split()
# dict = {}
#
#
# for i in str:
#     if i in dict:
#         print(f"{i}_{dict[i]}", end=" ")
#     else:
#         print(i, end=" ")
#     dict[i] = dict.get(i, 0) + 1
#

#
# word = input("Введите строку: ").split()
# result = {}
# for i in word:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#         result[i] += 1
#     else:
#         print(i, end=' ')
#         result[i] = 1


# stroka = 'a a a b c a a d c d d'
#
# def foo(stroka):
#     list_1 = stroka.split()
#     list_2 = []
#     dct = {}
#     for i in list_1:
#         if i in dct:
#             dct[i] += 1
#             list_2.append(f'{i}_{str(dct[i])}')
#         else:
#             list_2.append(i)
#             dct[i] = 0
#     return ' '.join(list_2)
#
# print(foo(stroka))

#
# s = 'a a a b c a a d c d d'
# s = s.split()
# print(s)
# final_string = ''
# for i in range(len(s)):
#     if s[0:i].count(s[i]) == 0:
#         final_string += f' {s[i]}'
#     else:
#         final_string += f' {s[i]}_{s[0:i].count(s[i])}'
# print(final_string)

#
# st = list(input("Введите строку: "))
# print(st)
# d = {}
# p = ""
# for i in range(len(st)):
#     if d.get(st[i]) != None:
#         d[st[i]] = int(d[st[i]])+1
#     else:
#         d[st[i]] = 1
#     p = p + f"{st[i]}_{d[st[i]]}"
# print(p)
#
#
# print('aBcdEfg.?,!'.strip('.?,!\n').lower())

# Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)

# num = int(input('Введите положительное число: '))
# max = 0
# while num != 0:
#     if num < 0:
#         print('Вы ввели отрицательное число.')
#     if num > max: max = num
#     num = int(input('Введите положительное число: '))
# print(f'Максимальное число: {max}')

from random import randint as rnd

lst = []
lst_max = []
n = rnd(19, 19)

def RandList(lst, n):
    for i in range(n):
        if i < n:
            lst.append(rnd(0, 29))
    print(lst)


def FindMaxElement(lst):
    max_element = 0
    for i in lst:
        if i != 0:
            lst_max.append(i)
            max_element = max(lst_max)
        else:
            break
    print(lst_max)
    print(max_element)

RandList(lst, n)
FindMaxElement(lst)
