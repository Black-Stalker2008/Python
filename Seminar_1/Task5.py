# 5. Напишите программу, которая принимает на вход число и проверяет,
#    кратно ли оно 5 и 10 или 15, но не 30.

# n = int(input())

# if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30:
#     print('Yes')
# else:
#     print('No')


print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x == z or x <= y and z):
                print(x,y,z)