# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
#  Играют два игрока делая ход друг после друга.
#   Первый ход определяется жеребьёвкой. 
#   За один ход можно забрать не более чем 28 конфет.

#    Все конфеты оппонента достаются сделавшему последний ход. 
#    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


from random import randint
candy = 100
player_choosing = 0
step = 0
Que = input('Вас двое? (Y/N):   ')
if (Que == 'N'):
    name1 = input('Введите ваше имя:   ')
    name2 = name1
else:
    name1 = input('Введите ваше имя:   ')
    name2 = input('Введите ваше имя:   ')










rnd = randint(0,1)
print (rnd)




while(True):
    if Que == 'N':
        
        if (rnd == 0):

            for i in range (1, 28 + 1):
                if (candy > 57):
                    player_choosing = 28
                    break
                elif (candy < 28):
                    player_choosing = 28 - candy
                elif (candy - 28 - 28 >28 ):
                    player_choosing = 28
                    break
            
                elif (candy - i == 29):
                    player_choosing = i
                    break
                elif (i < 28):
                    pass  
                elif (candy == 28 ):
                    player_choosing = 28  
                if (candy - i == 28 or candy - i == 0):
                    player_choosing = i
                    break
                
            
                else:
                    player_choosing = 28
        
            print (f'Ваш ход, м-сье Робот. Введите число(Осталось {candy} конфет):  {player_choosing}    ')  
            print (player_choosing)
            candy -= player_choosing
            rnd = 1
        elif (rnd == 1):
            if (candy == 0):
                print(f'М-сье Робот Выиграл! Вы неудачник!')
                candy = 0
                break   
            else:
                player_choosing = int(input(f'Ваш ход, {name1}. Введите число(Осталось {candy} конфет):     '))
                while (player_choosing > 28 or candy - player_choosing < 0):
                    print('Это число больше 28 или меньше нуля')
                    player_choosing = int(input(f'Ваш ход, {name1}. Введите число(Осталось {candy} конфет):     '))
                    
                else:
                    candy -= player_choosing
                    step += 1 
                    player_choosing = 0
                    rnd = 0
            
            print (player_choosing)
            if (candy == 0 and  step % 2 == 0): 
                
                print(f'{name2} Выиграл! Поздравляем!')
                candy = 0
                break  
            
        



    if Que == 'Y':

        if (rnd == 0):
        
            if (candy == 0):
                print(f'{name2} Выиграл! Поздравляем!') # выигрывает предыдущий игрок
                candy = 0
                break   






            else:
                player_choosing = int(input(f'Ваш ход, {name1}. Введите число(Осталось {candy} конфет):     '))
                if (player_choosing > 28 or candy - player_choosing < 0):
                    print('Это число больше 28 или меньше нуля')
                    pass
                else:
                    candy -= player_choosing
                    step += 1 
                    player_choosing = 0
                    rnd = 1






        if (rnd == 1):
            if (candy == 0): 
                print(f'{name1} Выиграл! Поздравляем!') # выигрывает предыдущий игрок
                candy = 0
                break






            else:
                player_choosing = int(input(f'Ваш ход, {name2}. Введите число(Осталось {candy} конфет):     '))
                if (player_choosing > 28 or candy - player_choosing < 0):
                    print('Это число больше 28 или меньше 0')
                else: 
                    candy -= player_choosing
                    step += 1 
                    player_choosing = 0
                    rnd = 0
            
    









