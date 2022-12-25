# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

def create_list(amount):
    new_list = sample(range(1, (amount+1)*2), k=amount)
    return new_list

def mulplication_list(new_list: list):
    mulpl_list = []
    len_list = len(new_list)
    
    for i in range(len_list//2):
            mulpl_list.append(new_list[i] * new_list[len_list - i - 1])

    if len_list % 2:
        mulpl_list.append(new_list[len_list // 2])
    return mulpl_list


res = create_list(int(input('Введите количество чисел в списке: ')))
print(res)
result = mulplication_list(res)
print(result)
