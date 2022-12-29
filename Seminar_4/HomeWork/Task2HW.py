# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

num = int(input("Задайте натуральное число N "))
i = 2 
list_simple = []
while i <= num:
    if num % i == 0:
        list_simple.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f'Список простых множителей числа N: {list_simple}')