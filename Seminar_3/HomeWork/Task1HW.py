# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample

def find_sum_odd_pos(amount):
    new_list = sample(range(1, (amount+1)*2), k=amount)
    print(new_list)
    sum_odd = 0
    for i in range(0, len(new_list), 2):
        sum_odd = sum_odd + new_list[i]
    return sum_odd

result = find_sum_odd_pos(int(input('Введите количество чисел в списке: ')))
                          
print(f'Сумма элементов списка, стоящих на нечётных позициях, равна {result}')
