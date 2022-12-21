

pole=[['1,1','1,2','1,3'],['2,1','2,2','2,3'],['3,1','3,2','3,3']]

print(*pole, sep='\n')


i = 0

def krestiki_step (i):

    
    while i <=5:
        xx= int(input('крестики введите координаты по горизонтали от 1 до 3   '))
        if xx !=int(1) or int(2) or int(3):
            print("введите число от 1 до 3")
        xy= int(input('крестики введите координаты по вертикали от 1 до 3   '))
        if (pole[xx-1][xy-1] == 'X' or pole[xx-1][xy-1] == 'O'):
            print('место занято')
            krestiki_step(i)
        pole[xx-1][xy-1]='X'
        print(*pole, sep='\n')
        if (pole[0][0]==pole[0][1]==pole[0][2]=="X") or (pole[1][0]==pole[1][1]==pole[1][2]=="X") or (pole[2][0]==pole[2][1]==pole[2][2]=="X") or (pole[0][0]==pole[1][0]==pole[2][0]=="X") or (pole[0][1]==pole[1][1]==pole[2][1]=="X") or (pole[2][0]==pole[2][1]==pole[2][2]=="X") or (pole[0][0]==pole[1][1]==pole[2][2]=="X") or (pole[0][2]==pole[1][1]==pole[2][0]=="X"):
      
            print("выиграли крестики")
            break
        elif (pole[0][0]==pole[0][1]==pole[0][2]=="O") or (pole[1][0]==pole[1][1]==pole[1][2]=="O") or (pole[2][0]==pole[2][1]==pole[2][2]=="O") or (pole[0][0]==pole[1][0]==pole[2][0]=="O") or (pole[0][1]==pole[1][1]==pole[2][1]=="O") or (pole[2][0]==pole[2][1]==pole[2][2]=="O") or (pole[0][0]==pole[1][1]==pole[2][2]=="O") or (pole[0][2]==pole[1][1]==pole[2][0]=="O"):
      
            print("выиграли нолики")
            break
        if (i == 9):
            print("ничья")
            break
        else:
            i +=1
            noliki_step(i)
            return i
def noliki_step (i):
    while i <= 4:
        ox= int(input('нолики введите координаты по горизонтали от 1 до 3   '))
        oy= int(input('нолики введите координаты по вертикали от 1 до 3   '))
        if (pole[ox-1][oy-1] == 'X' or pole[ox-1][oy-1] == 'O'):
            print('место занято')
            noliki_step(i)
        pole[ox-1][oy-1]='O'
        print(*pole, sep='\n')
    


        if (pole[0][0]==pole[0][1]==pole[0][2]=="X") or (pole[1][0]==pole[1][1]==pole[1][2]=="X") or (pole[2][0]==pole[2][1]==pole[2][2]=="X") or (pole[0][0]==pole[1][0]==pole[2][0]=="X") or (pole[0][1]==pole[1][1]==pole[2][1]=="X") or (pole[2][0]==pole[2][1]==pole[2][2]=="X") or (pole[0][0]==pole[1][1]==pole[2][2]=="X") or (pole[0][2]==pole[1][1]==pole[2][0]=="X"):
      
            print("выиграли крестики")
            break
        elif (pole[0][0]==pole[0][1]==pole[0][2]=="O") or (pole[1][0]==pole[1][1]==pole[1][2]=="O") or (pole[2][0]==pole[2][1]==pole[2][2]=="O") or (pole[0][0]==pole[1][0]==pole[2][0]=="O") or (pole[0][1]==pole[1][1]==pole[2][1]=="O") or (pole[2][0]==pole[2][1]==pole[2][2]=="O") or (pole[0][0]==pole[1][1]==pole[2][2]=="O") or (pole[0][2]==pole[1][1]==pole[2][0]=="O"):
      
            print("выиграли нолики")
            break
        elif (i == 9):
            print('ничья')
            break
        else:
            
            krestiki_step(i)
            return i
            
krestiki_step(i) 
print()  
if (i == 9):     
    print ('ничья') 