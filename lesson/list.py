# # Заполнить массив нулями, кроме первого и последнего элементов, которые должны быть равны единице.
# a4 = []
# for i in range(10):
#     a4.append(0)
# print(a4)
#
# a1 = a4.insert(0, 1)
# a2 = a4.insert(-1, 1)
# a3 = a4.pop(9)
# print(a4)
#
# # Заполнить массив нулями и единицами, при этом данные значения чередуются, начиная с нуля.
# a5 = []
# for i in range(10):
#     a5.append(0)
#     a5.append(1)
# print(a5)
#
# Заполнить массив последовательными нечетными числами, начиная с единицы.
# number = 0
# a6 = []
# for index in range(11):
#     a6.append(1)
#     if a6[index] < a6[index+1]:
#          number +=2
# print(number)
# def list():
#     a = []
#     number = 0
#     for i in range(2):
#         a.append(1)
#         for elem in a:
#             if a[elem] < a[index +1]:
#               number += 1
#               print(number)
#
# list()

# Сформировать возрастающий массив из четных чисел.
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = []
# for i in a:
#     if a[i] // 2:
#         b.append(a)
# print(b)


# c = []
#
# for i in range(0,11):
#     if i % 2 == 0:
#         c.append(i)
# print(c)
# import random
# c1 = []
# for i in range(random.randint(1,21)):
#     if i % 2 == 0:
#         c1.append(i)
# print(c1)
#
# x = list(range(0,23,2))
# print(x)

# # Чтобы выводился массив с нечётными чилами
# import random
# c1 = []
# for i in range(random.randint(1,21)):
#     if i % 3 == 1:
#         c1.append(i)
# print(c1)
#
# x1 = list(range(1,101,2))# вывод нечётных чисел
# print(x1)

# Создать массив из случайных значений
# from random import randint
# c2 = [randint(0,1000) for i in range(1000)]
# print(c2)
# # Создать многомерный массив со случайными значениями (вложенные списки)
# from random import randint
# c3 = [[randint(0,1000), randint(0,1009) ]for i1 in range(200)]
# print(c3)

# Сформировать убывающий массив из чисел, которые делятся на 3.
# c = []
# for i in range(0,13):
#     if i % 3 == 0:
#         c.append(i)
#         c.reverse()
# print(c)

# Заполнить массив заданной длины различными простыми числами. Натуральное число, большее единицы, называется простым, если оно делится только на себя и на единицу.
# f = list(range(0, 100, 2))
# print(f)
#
# f1 = []
# for i in range(0,100):
#     if i % 1 == 0 and i % 2 == 0:
#         f1.append(i)
# print(f1)


# Создать массив, каждый элемент которого равен квадрату своего номера.
# v = []
# for i in range(0,100):
#     v.append(i**2)
# print(v)
# x = []
# for i in range(1000):
#     x.append(i)
#     if x[i] == i*i:
#         x.append(i)
# print(x)

# r = list(range(1000))
# for i in r:
#     if r[i] == i:
#         r.append(i)
# print(r)
# #
# x = []
# c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for i in c:
#     if c[i] == i * i:
#         x.append(i)
# print(x)


# Создать массив, который одинаково читается как слева направо, так и справа налево.
# y = list(range(0, 21))
# c = list(range(0, 21))  # c[::-1]  #c = list(range(0,21)).reverse()
# c = c[::-1]
# print(y + c)

# Определить, содержит ли массив данное число x
# f = [1,2,3,4,5,5,6,6]
# a = 1
# for i in f:
#     if i == a:
#         print("капуста")
#     else:
#         print("помидор")

# Найти количество четных чисел в массиве.
# g = [1,2,3,4,5,6,7,8,9,10]
# count = 0
# for i in g:
#     if i % 2:
#         count +=1
#         print("чётные числа:", count)
#     else:
#         print("error")
#

# Найти количество чисел в массиве, которые делятся на 3, но не делятся на 7.
# h = [3, 4, 5, 6, 7, 21, 39, 48, 49]
# count = 0
# for i in h:
#     if i % 3 == 0:
#         count += 1
#         print(count)
#     elif i is not i % 7:
#         print("cocous")
#     else:
#         print('err')

# Найдите сумму и произведение элементов массива.
# c = []
# s = [1, 2, 3, 4]
# print(sum(s))
# for p in range(1):
#     for i in s:
#         if i in s:
#             c.append((i * i) * i)
# print(c)
