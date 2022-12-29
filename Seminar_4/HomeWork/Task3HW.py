# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randrange

def create_list(amount):
    new_list = []
    for i in range (0, amount):
        num = randrange(0, 99, 1)
        new_list.append(num)
    if amount <= 0:
        print("Negative value of the number of numbers!")    
    return new_list

def return_unique(new_list):
    result_list = []
    for i in new_list:
        if new_list.count(i) < 2:
            result_list.append(i)
    return result_list

list = create_list(int(input('Введите количество чисел в списке: ')))
print(list)

res_list = return_unique(list)
print(res_list)