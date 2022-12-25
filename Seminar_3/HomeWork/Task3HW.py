# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

def decimalToBinary(num: int):
    list_bin = []

    while num > 0:
        list_bin.insert(0, num % 2)
        num //= 2

    print(*list_bin, sep="")

decimalToBinary(int(input()))
