# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

import random

word = "абв"
num = (int(input("Number of words: ")))

print("Random text: ")
list_word = []
for i in range(num):
    random_text = random.sample(word, 3)
    list_word.append("".join(random_text))
print(" ".join(list_word))

print()
list_word2 = list(filter(lambda x: word not in x, list_word))
print(" ".join(list_word2))