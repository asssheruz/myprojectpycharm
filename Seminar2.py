# По данному целому неотрицательному n вычислите значение
# n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
#
# Input:       5
# Output:    120
#
# flag = True
# a = 0
# while a < 5 and flag:
#     print(a)
#     a += 1
while flag:
    print(1)
    if 5 > 1
        flag = False
# Дано натуральное число A > 1. Определите, каким по счету числом
# Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
#
# Input:     5
#
# Output:  6
print("Enter n")
n=int(input())

res1=1
res2=1
res=0
i=2
while res<n:
    res=res1+res2
    res1=res2
    res2=res
    i+=1


if n!=res:
    print(-1)
else:
    print(res,i,sep=" ")

