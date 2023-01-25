# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

n = int(input("Введите количество элементов первого набора чисел: "))
m = int(input("Введите количество элементов второго набора чисел: "))
import random
my_listn = []
for i in range(n):
    my_listn.append(random.randint(1, 10))
print(my_listn)
my_listm = []
for i in range(m):
    my_listm.append(random.randint(1, 10))
print(my_listm)
result = []
for item in my_listn:
    if item in my_listm:
        result.append(item)
result.sort
result_list = list(set(result))
print(result_list)