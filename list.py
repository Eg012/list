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
def list():
    a = []
    number = 0
    for i in range(2):
        a.append(1)
        for index in a:
            if a[index] < a[index +1]:
              number += 1
              print(number)

list()