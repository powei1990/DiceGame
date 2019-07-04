import random
import numpy as np

def roll(player):
    score = 0
    throw_times=0
    if player==0:
        print("---莊家---")
        input("按Enter擲骰")
    else:
        print("---閒家%i---"%player)
    while not score:

        point=[random.choice(dice) for a in range(4)]
        throw_times+=1
        print("第%i次投擲"%throw_times)
        print(point)
        score=check(point)
        if score>0:
            input("按Enter繼續")
        #print(score)
    return score

def check(point):
    for i in range(1,7):
        if point.count(i)==6:
            score=18
            print("%i點一色"%i)
            #isconfirm=True
            return score
        elif point.count(i)==2:
            #print("%i confirm"%i)
            score=sum(list(filter(lambda n:n!=i,point)))
            print("%i點"%score)
            #isconfirm=True
            #print(point)
            return score
            break
    print("沒點")
    return 0



def judge(matrix,num_of_player,bet):
    print("************")
    for i in range(0,num_of_player):
        if matrix[i][1]>0:
            if i==0:
                print("莊家")
                print("%i點"%matrix[i][0])
            else:
                print("閒家%i"%i)
                print("%i點"%matrix[i][0])
            #閒家獲勝
            if matrix[i,0]>matrix[0,0]:

                print("獲勝")
                matrix[i,1]+=bet
                matrix[0,1]-=bet
            #閒家落敗
            elif matrix[i,0]<matrix[0,0]:
                print("落敗")
                matrix[i,1]-=bet
                matrix[0,1]+=bet
            #莊家一色通吃
            elif matrix[0,0]==18:
                matrix[1:,1]-=bet
                matrix[0,1]+=bet*num_of_player-1
                print("莊家一色通吃")
            #閒家一色加倍
            elif matrix[i,0]==18:
                matrix[i,1]+=bet*2
                matrix[0,1]-=bet*2
                print("一色加倍")
            if matrix[i,1]<=0:
                print("破產!")
        print("-----------")
    print("************")
    if matrix[0][1]<=0:
        print("你輸了!")
        show_record(matrix,num_of_player)
        print("遊戲結束")
        input("按Enter結束")
        return True
    elif max(matrix[1:,1])<=0:
        print("你贏了!")
        show_record(matrix,num_of_player)
        input("按Enter結束")
        return True
    else:
        return False
    #print(matrix)  
        

def game_start(matrix,num_of_player):
    for i in range(0,num_of_player):
        if matrix[i][1]>0:
            matrix[i][0]=roll(i)

def show_record(matrix,num_of_player):
    for i in range(0,num_of_player):
        if i==0:
            print("莊家 :%d"%matrix[0][1])
        else:
            print("閒家%i:"%i+"%d"%matrix[i][1])
        


print ("***擲骰子遊戲***")
win, lose = 0, 0
dice = [i for i in range(1,7)]
num_of_player=int(input("多少閒家:"))+1
money=int(input("起始金額:"))
#生成num_of_player列的二維list
matrix=np.zeros((num_of_player,2))
matrix[0:,1]=money
bet=int(input("下注金額:"))
game_start(matrix,num_of_player)
is_gameover=judge(matrix,num_of_player,bet)
while not is_gameover:
    #elif is_gameover==True:
    play = input('是否繼續(y/n)?剩餘金額(h)')
    if play in ('Y', 'y'):
        bet=int(input("下注金額:"))
        game_start(matrix,num_of_player)
        is_gameover=judge(matrix,num_of_player,bet)
    elif play in ('H','h'):
        show_record(matrix,num_of_player)
    elif play in ('n', 'N'):
        #print ('目前戰績%s勝%s負' % (win, lose))
        print ('Good Bye!')
        break
    
        
        
        

