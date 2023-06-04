# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint as rd

# list = []
#
# while True:
#     try:
#         n = int(input("Введите количество элементов списка: "))
#         a = int(input("Какое число проверить на повторы: "))
#         break
#     except ValueError:
#         print("Введите целое число, а не букву!")
#
#
# def RandomList(list, n):
#     for i in range(n):
#         if i < n:
#             list.append(rd(1, 9))
#     return list
#
#
# def FindElements(list, a):
#     count = 0
#     for i in list:
#         if i == a:
#             count += 1
#     return count
#
#
# print("Печатаем список:", *RandomList(list, n))
# print("Количество повторяющихся элементов:", FindElements(list, a))


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# from random import randint as rd
#
# list = []
# list_1 = []
# while True:
#     try:
#         n = int(input("Введите количество элементов списка: "))
#         a = int(input("К какому числу ищем самый близкий по величине элемент: "))
#         break
#     except ValueError:
#         print("Введите целое число, а не букву!")
#
#
# def RandomList(list, n):
#     for i in range(n):
#         if i < n:
#             list.append(rd(1, 99))
#     return list
#
#
# def CloseElement(list, list_1, a):
#     close_element = list[0]
#     for i in list:
#         if i < a:
#             list_1.append(i)
#             close_element = max(list_1)
#     return close_element
#
# print("Выводим список:", RandomList(list, n))
# print("Выводим отсортированный лист:", sorted(list))
# print("Минимально близкий элемент:",
#       CloseElement(list, list_1, a))



# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

import re

word = input("Введите любое слово: ")
word = word.upper()

rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}

def RusOrEng(word):
    return bool(re.search("[а-яА-Я]", word))

if RusOrEng(word):
    print("Сумма баллов:", sum([k for i in word for k, v in rus.items() if i in v]))
else:
    print("Сумма баллов:", sum([k for i in word for k, v in eng.items() if i in v]))
