# НАБОР ФУНКЦИЙ к ЗАДАЧЕ:  Ex5_sum_polynom  Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random

def creat_p_if_deg1(coeff):
    polynom_string = ''
    if coeff[0] > 1 and coeff[1] > 0:
        polynom_string = str(coeff[0]) + \
            'x + ' + str(coeff[1]) + ' = 0'
    elif coeff[0] > 1 and coeff[1] == 0:
        polynom_string = str(coeff[0]) + 'x = 0'
    elif coeff[0] == 1 and coeff[1] > 0:
        polynom_string = 'x + ' + str(coeff[1]) + ' = 0'
    elif (coeff[0], coeff[1]) == (1, 0):
        polynom_string = 'x = 0'
    return polynom_string

def p_ended(deg, coeff):
    polynom_ended = ''
    if coeff[deg - 1] > 1:
        polynom_ended += '+ ' + \
        str(coeff[deg - 1]) + 'x + ' + \
        str(coeff[deg]) + ' = 0'
    elif (coeff[deg - 1], coeff[deg]) == (1, 0):
        polynom_ended += '+ x = 0'
    elif (coeff[deg - 1], coeff[deg]) == (0, 0):
        polynom_ended += ' = 0'
    elif coeff[deg - 1] == 0 and coeff[deg] != 0:
        polynom_ended += '+ ' + str(coeff[deg]) + ' = 0'
    elif (coeff[deg - 1], coeff[deg]) == (1, 1):
        polynom_ended += '+ x + ' + \
        str(coeff[deg]) + ' = 0'
    return polynom_ended

def creat_polynom(deg):
    coeff = [random.randint(0, 100) for i in range(deg + 1)]
    print(f'Коэффициенты полинома: {coeff}, если первый коэф. = "0", \n \
        он будет заменен другим случ. числом')
    if coeff[0] == 0:
        coeff[0] = random.randint(1, 100)
    if deg > 1:
        if coeff[0] > 1:
            polynom_string = str(coeff[0])+'x^' + str(deg) + ' '
        elif coeff[0] == 1:
            polynom_string = 'x^' + str(deg) + ' '
        count = deg - 1
        while count > 1:
            if coeff[deg - count] != 0:
                if coeff[deg - count] > 1:
                    polynom_string += '+ ' + \
                        str(coeff[deg - count]) + \
                        'x^' + str(count) + ' '
                elif coeff[deg - count] == 1:
                    polynom_string += '+ ' + \
                        'x^' + str(count) + ' '
            count -= 1
        if count == 1:
            polynom_string += p_ended(1, [coeff[-2], coeff[-1]])
    elif deg == 1:
        polynom_string = creat_p_if_deg1(coeff)
    elif deg < 1:
        print('Степень введена некорректно!')
        return
    return polynom_string


def nul_coef(m_deg, str_deg):
    if int(m_deg) > len(str_deg)-1:
        str_deg = list(map(int, str_deg.split()))
        str_deg.revers()
        for i in range(len(str_deg)):
            if int(str_deg[i])-1 != int(str_deg[i-1]):
                str_deg.insert(int(str_deg[i])-1, 0)
        str_deg.revers()
    return str_deg


def lst_deg(data):
    deg_str = []
    while 'x' in data:
        space_pos = data.index('x')
        if data[space_pos+2].isdigit():
            deg_str.append(data[space_pos+2])
            data = data[space_pos+5:]
        elif not data[space_pos+2].isdigit():
            data = data[space_pos+3:]
    deg_str.extend(['1', '0'])
    deg_polyn = nul_coef(deg_str[0], deg_str)
    deg_polyn = list(map(int, deg_polyn))
    return deg_polyn


def lst_coef(data):
    coef_str = []
    while 'x' in data:
        space_pos = data.index('x')
        if data[space_pos-1] != ' ':
            coef_str.append(int(data[: space_pos]))
        else:
            coef_str.append(int('1'))
        if data[space_pos+1] == ' ':
            coef_str.append(int(data[space_pos+3:]))
        data = data[space_pos + 5:]
    # coef_polyn = list(map(int, coef_str))
    return coef_str


def creat_polynom1(deg, coeff):
    print(f'Коэффициенты нового полинома: {coeff}')
    if coeff[0] == 0:
        coeff[0] = random.randint(1, 100)
    if deg > 1:
        if coeff[0] > 1:
            polynom_string = str(coeff[0])+'x^' + str(deg) + ' '
        elif coeff[0] == 1:
            polynom_string = 'x^' + str(deg) + ' '
        count = deg - 1
        while count > 1:
            if coeff[deg - count] != 0:
                if coeff[deg - count] > 1:
                    polynom_string += '+ ' + \
                        str(coeff[deg - count]) + \
                        'x^' + str(count) + ' '
                elif coeff[deg - count] == 1:
                    polynom_string += '+ ' + \
                        'x^' + str(count) + ' '
            count -= 1
        if count == 1:
            polynom_string += p_ended(1, [coeff[-2], coeff[-1]])
    elif deg == 1:
        polynom_string = creat_p_if_deg1(coeff)
    return polynom_string




# def nul_coef(m_deg, str_deg):
#     if int(m_deg) > len(str_deg)-1:
#         str_deg = list(map(int, str_deg.split()))
#         str_deg.revers()
#         for i in range(len(str_deg)):
#             if int(str_deg[i])-1 != int(str_deg[i-1]):
#                 str_deg.insert(int(str_deg[i])-1, 0)
#         str_deg.revers()
#     return str_deg
                
# def lst_deg(data):
#     deg_str = []
#     while 'x' in data:                                
#         space_pos = data.index('x')
#         if data[space_pos+2].isdigit():
#             deg_str.append(data[space_pos+2])
#             data = data[space_pos+5:]
#         elif not data[space_pos+2].isdigit():  
#             data = data[space_pos+3:]
#     print(data)
#     deg_str.extend(['1', '0'])
#     str_deg_polyn = ' '.join(deg_str)
#     deg_polyn = nul_coef(deg_str[0], str_deg_polyn)
#     ls_deg_polyn = list(map(int, ls_deg_polyn.split()))
#     return deg_polyn

# def lst_coef(data):
#     coef_str = []
#     while 'x' in data:
#         space_pos = data.index('x')
#         if data[space_pos-1] != ' ':
#             coef_str.append(int(data[: space_pos]))
#         else:
#             coef_str.append(int('1'))
#         data = data[space_pos + 5:]
#     coef_str.extend(data)
#     coef_polyn = list(map(int, coef_str))
#     return coef_polyn
