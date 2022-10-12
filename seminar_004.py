# ЗАДАЧА 1 (К ЧЕТВЕРТОМУ СЕМИНАРУ ПО PYTHON)
# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}




# ЗАДАЧА 2 (К ЧЕТВЕРТОМУ СЕМИНАРУ ПО PYTHON)
# Задайте натуральное число N. 
# # Напишите программу, которая составит список простых множителей числа N.
# и числа {old} приведены в списке: {lst}")


# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")








# ЗАДАЧА 3 (К ЧЕТВЕРТОМУ СЕМИНАРУ ПО PYTHON)
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")




    
# ЗАДАЧА 4 (К ЧЕТВЕРТОМУ СЕМИНАРУ ПО PYTHON)
# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# -  k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0


# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('33_Polynomial.txt', 'w') as data:
#     data.write(polynom1)


# Второй многочлен для следующей задачи:

# k = randint(2, 5)

# ratios = get_ratios(k) 
# polynom2 = get_polynomial(k, ratios)
# print(polynom2)

# with open('33_Polynomial2.txt', 'w') as data:
#     data.write(polynom2)











# ЗАДАЧА 5 (К ЧЕТВЕРТОМУ СЕМИНАРУ ПО PYTHON)
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# with open('poly_1.txt', 'w', encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x^5')
# with open('poly_2.txt', 'w', encoding='utf-8') as file:
#     file.write('23*x^4 + 9*x^6')

# with open('poly_1.txt','r') as file:
#     poly_1 = file.readline()
#     list_of_poly_1 = poly_1.split()


# with open('poly_2.txt','r') as file:
#     poly_2 = file.readline()
#     list_of_poly_2 = poly_2.split()

# print(f'{list_of_poly_1} + {list_of_poly_2}')
# sum_poly = list_of_poly_1 + list_of_poly_2

# with open('sum_poly.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_poly_1} + {list_of_poly_2}')
