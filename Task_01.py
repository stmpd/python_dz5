
#Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
#in
#Number of words: 10
#out
#авб абв бав абв вба бав вба абв абв абв
#авб бав вба бав вба


from random import choices


def fill(num):
    result = []
    for i in range(num):
        result.append("".join(choices("абв", k=3)))
    return " ".join(result)


def removing(lst):
    return lst.replace("абв", "").replace("  ", " ")


n = int(input("Введите количество наборов букв: "))
list = fill(n)
print(list)
print(removing(list))