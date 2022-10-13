# ЗАДАЧА 1 (К ПЯТОМУ СЕМИНАРУ ПО PYTHON)
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. В
# се конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# ВАРИАНТ (А)
# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x

# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")



# ВАРИАНТ (Б)
# import random
# from random import randint, choice
 
# print(
#     '"Игра с конфетами"\n'
#     'В игре участвуют два игрока\n'
#     'Первый ход определяется жеребьевкой.\n'
#     'Игроки ходят, совершая ход друг после друга\n'
#     'Правила игры\n'
#     'У нас есть некоторое количество конфет\n'
#     'За один ход можно забрать не более определенного количества конфет, о котором мы договоримся\n'
#     'Тот, кому достанется последняя конфета - проиграл\n'
#     )
 
# messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
#             'сколько конфет берем?', 'берите еще', 'Ваш ход']
# max_number_move = 0
 
# def introduce_players():
#     player1 = input('Первый игрок, представьтесь\n')
#     player2 = 'CompBOT'
#     print(f'Очень приятно, сегодня Вы играете с искуственным  {player2}')
#     return [player1, player2]
 
# def sweets_game(players):
#     global max_number_move
#     total_sweets = int(input('Введите cколько всего у нас конфет:\n'))
#     max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
#     first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#     if first != 1:
#         first = 0
#     return [total_sweets, max_number_move, int(first)]
 
# max_move = max_number_move
 
# def game_player_vs_smart_bot(sweets, players, messages):
#     global max_number_move
#     count = sweets[2]
 
 
#     while sweets[0] > 0:
#         if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
#             move = sweets[0] -1
#             print(f'Я забираю {move}')
 
#         elif not count % 2:
#             move = random.randint(1, sweets[1])
#             print(f'Я забираю {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > sweets[0] or move > sweets[1]:
#                 print(
#                     f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
#                 chance = 2
#                 while chance > 0:
#                     if sweets[0] >= move <= sweets[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {chance} попытки')
#                     move = int(input())
#                     chance -= 1
#                 else:
#                     return print(f'Попыток не осталось. Game over!')
#         sweets[0] = sweets[0] - move
#         if sweets[0] > 0:
#             print(f'Осталось {sweets[0]} конфет')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]
 
 
# players = introduce_players()
# sweets = sweets_game(players)
 
# winer = game_player_vs_smart_bot(sweets, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(
#         f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')


# ЗАДАЧА 2 (К ПЯТОМУ СЕМИНАРУ ПО PYTHON)
# Создайте программу для игры в ""Крестики-нолики""

# maps = [1, 2, 3,
#         4, 5, 6,
#         7, 8, 9]

# victories = [[0, 1, 2],
#              [3, 4, 5],
#              [6, 7, 8],
#              [0, 3, 6],
#              [1, 4, 7],
#              [2, 5, 8],
#              [0, 4, 8],
#              [2, 4, 6]]

# def print_maps():                       # вывод карты на экран
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8]) 


# def step_maps(step,symbol):              # Сделать ход в ячейку
#     ind = maps.index(step)
#     maps[ind] = symbol



# def get_result():                       # Получить текущий результат игры
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win


# game_over = False
# player1 = True
 
# while game_over == False:
 
#     # вывод карты поля
#     print_maps()
 
    
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Игрок 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Игрок 2, ваш ход: "))
 
#     step_maps(step,symbol) # делаем ход в указанную ячейку
#     win = get_result() # определим победителя
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
 
#     player1 = not(player1)        
 
     
# print_maps()
# print("Победил", win)




# ЗАДАЧА 3 (К ПЯТОМУ СЕМИНАРУ ПО PYTHON)
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def rle_encode(data):  (вариант решения с ошибкой, еще доработаю.... времени мало)
#     encoding = '' 
#     prev_char = '' 
#     count = 1 
#     if not data: 
#         return '' 
#         for char in data: 
       
#             if prev_char: 
#                 encoding += str(count) + prev_char 
#             count = 1 
#             prev_char = char 
#         else: 
           
#             count += 1 
#     else: 
#         encoding += str(count) + prev_char 
#         return (encoding)


# def rle_decode(data): 
#     decode = '' 
#     count = '' 
#     for char in data: 
   
#         if char.isdigit(): 
   
#         count += char 
#     else: 
     
#         decode += char * int(count) 
#         count = '' 
#     return (decode)


# decoded_val = rle_decode('6A1F2D7C1A17E') 
# print(decoded_val)


# ВАРИАНТ РЕШЕНИЯ ЧЕРЕЗ ДВОЙКУ:
# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 2
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")
