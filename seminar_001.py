# ЗАДАЧА 1 (К ПЕРВОМУ СЕМИНАРУ ПО PYTHON)
#  Напишите программу, которая Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# day = int(input('Day number: '))
# if day > 7 or day < 1:
#     print('Please, repeat the input')
# if day == 6 or day == 7:
#     print("Yes, it's weekend!")
# else:
#     print("No, it's not weekend!")


# Вариант решения одогруппника/
# day_number = int(input("Введите номер дня недели: "))

# if 0 < day_number < 8:
#     if day_number > 5:
#         print("yes")
#     else:
#         print("no")
# else:
#     print("Введите корректный номер дня недели")



# ЗАДАЧА 2 (К ПЕРВОМУ ДСЕМИНАРУ ПО PYTHON)
#  Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))
#                 print(x, y, z)

# ЗАДАЧА 3 (К ПЕРВОМУ СЕМИНАРУ ПО PYTHON)
# Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).


# x = int(input('input x: '))
# y = int(input('input y: '))
# if x > 0 and y > 0:
#     print('1')
# if x < 0 and y > 0:
#     print('2')
# if x < 0 and y < 0:
#     print('3')
# if x > 0 and y < 0:
#     print('4')


# ЗАДАЧА 4 (К ПЕРВОМУ СЕМИНАРУ ПО PYTHON)
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


# n = int(input('input quarter number: '))
# if n < 1 or n > 4:
#     print('Please, repeat the input')
# elif n == 1:
#     print('x > 0 and y > 0')
# elif n == 2:
#     print('x < 0 and y > 0')
# elif n == 3:
#     print('x < 0 and y < 0')
# elif n == 4:
#     print('x > 0 and y < 0')


# ЗАДАЧА 5 (К ПЕРВОМУ СЕМИНАРУ ПО PYTHON)
# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

# print('Enter coordinates point А:')
# x_A = float(input('X: '))
# y_A = float(input('Y: '))
# print("Enter coordinates point B:")
# x_B = float(input('X: '))
# y_B = float(input('Y: '))

# from math import sqrt
# print('Distance between A and B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2)) 