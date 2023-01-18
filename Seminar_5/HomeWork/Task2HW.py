# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# in
# Enter the data_2 of the file with the data_1:
# 'text_words.txt'
# Enter the file data_2 to record:
# 'text_code_words.txt'
# Enter the data_2 of the file to decode:
# 'text_code_words.txt'

from itertools import groupby, starmap
from os import path


def rle_encode(data_1="text_words.txt", code_data="text_code_words.txt"):
    if path.exists(data_1):
        with open(data_1) as f_1, \
                open(code_data, "a") as f_2:
            for i in f_1:
                f_2.write("".join([f"{len(list(count))}{char}" for char, count in groupby(i)]))
    else:
        print("Файлы не существуют в системе")


def rle_decode(data_2):
    if path.exists(data_2):
        with open(data_2) as f:
            n = ""
            for k in f:
                nums_word = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        nums_word.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda a, b: a * b, nums_word)))
    else:
        print("Файлы не существуют в системе")

rle_encode(input("Введите название файла с текстом: "), input("Введите название файла для записи: "))
rle_decode(input("Введите название файла для декодирования: "))
