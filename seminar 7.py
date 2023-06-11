# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке,
# в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива.

# n = int(input("Введите количество элементов первого списка: "))
# m = int(input("Введите количество элементов второго списка: "))
# lst1 = []
# lst2 = []
# def first_lst(lst1, n):
#     for i in range(n):
#         lst1.append(int(input(f"Введитете {i+1} элемент списка: ")))
#     return lst1
# def second_lst(lst2, m):
#     for i in range(m):
#         lst2.append(int(input(f"Введитете {i+1} элемент списка: ")))
#     return lst2
# def list_compare(lst1, lst2):
#     for i in lst1:
#         if i in lst2:
#             lst1.remove(i)
#     return lst1
#
# print("Выводим первый список", first_lst(lst1, n))
# print("Выводим второй список", second_lst(lst2, m))
# print("Этих элементов нет во втором списке", list_compare(lst1, lst2))

# ------------------------------------------------------------------------------------------


# first_size = int(input('Введите количество элементов первого массива: '))
#
# print(first_array := [int(input(f'Введите элемент: ')) for _ in range(first_size)])
#
# second_size = int(input('Введите количество элементов второго массива: '))
#
# print(second_array := [int(input(f'Введите элемент: ')) for _ in range(second_size)])
#
# print(result_array := [i for i in first_array if i not in second_array])

# ---------------------------------------------------------------------------------------


# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество
# элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# import random
# list_size = int(input("Введите размер списка: "))
# print(list_1 := [random.randint(0, 10) for i in range(list_size)])
# count = 0
# for i in range(1, len(list_1)-1):
#     if list_1[i-1] < list_1[i] > list_1[i+1]:
#         count += 1
# print(count)

# --------------------------------------------------------------------------------------------

# Задача 43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается,
# что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# import random
# list_size = int(input("Введите количество элементов массива: "))
# list_1 = [random.randint(0, 10) for i in range(list_size)]
# list_2 = list_1.copy()
# count = 0
# for i in range(list_size-1):
#     for j in range(i + 1, list_size):
#         if list_2[i] == list_2[j]:
#             count +=1
#             list_2.pop(i)
#             list_2.pop(j)

a = int(input("Введите количество элементов списка: "))

b = [int(input()) for i in range(a)]

def pars_elements(b):
    count = 0
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            if b[i] == b[j]:
                count += 1
    print(count)

print(b)
pars_elements(b)
