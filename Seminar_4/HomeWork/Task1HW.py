# Вычислить число c заданной точностью d
# in
# Enter a real num: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

from decimal import Decimal

num = Decimal(input("Enter a real num: "))
accuracy = str(input("Enter the required accuracy '0.0001' "))
print(num.quantize(Decimal(accuracy)))