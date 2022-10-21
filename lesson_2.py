# Задние_1
#
# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# my_list = [12, 'name', (1, 3, 4), [32, 45, 6], False, 2.4, None, 2:4]
# for a in my_list:
#     print(type(a))
# -----------------------------------------------------------------------------------------------------------------------
# Задание_2
#
# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

# colichestvo = int(input('Введите количество элементов списка: '))
# my_list = []
# i = 0
# while i < colichestvo:
#     my_list.append(input('Введите значение списка: '))
#     i = i + 1
#
# col = 0
# for cl in range(int(len(my_list) / 2)):
#     my_list[col], my_list[col + 1] = my_list[col + 1], my_list[col]
#     col = col + 2
# print(my_list)

# Задание_3

# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

# month = int(input('Введите номер месяца: '))
# seasons_list = ['winter', 'spring', 'summer', 'autumn']
# if month == 12 or month == 1 or month == 2:
#     print(seasons_list[0])
# elif month == 3 or month == 4 or month ==5:
#     print(seasons_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_list[2])
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_list[3])
# else:
#     print("Такого месяца не существует")

# month = int(input('Введите номер месяца: '))
# seasons_dict = {
#     1: 'winter',
#     2: 'spring',
#     3: 'summer',
#     4: 'autumn'
# }
# if month == 12 or month == 1 or month == 2:
#     print(seasons_dict.get(1))
# elif month == 3 or month == 4 or month ==5:
#     print(seasons_dict.get(2))
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_dict.get(3))
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_dict.get(4))
# else:
#     print("Месяц неизвестен ")

# Задние_4
#
# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

# my_file = input('Введите несколько слов ')
# my_list = []
# number = 1
# for a in range(my_file.count(' ') + 1):
#     my_list = my_file.split()
#     if len(str(my_list)) <= 10:
#         print(f" {number} {my_list [a]}")
#         number += 1
#     else:
#         print(f" {number} {my_list [a] [0:10]}")
#         number += 1

# Задание_5
# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтингесуществуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

# my_list = [7, 5, 3, 3, 2]
# num = int(input('Введите число:'))  # 3
# i = 0
# for el in my_list:
#     if num <= el:
#         i += 1
# my_list.insert(i, num)
# print(my_list)
#
# list = [7, 5, 3, 3, 2]
# a = int(input('Введите новый элемент рейтинга: '))
# list.insert(min([len(list)] + [i for i, v in enumerate(list) if v < a]), a)
# print(list)