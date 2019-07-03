#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import numpy as np

def roll():
    score = 0
    while not score:
        point=[random.choice(dice) for a in range(4)]
        print(point)
        score=check(point)
        #print(score)
    return score

def check(point):
    for i in range(6):
        if point.count(i)==6:
            score=18
            #isconfirm=True
            return score
        elif point.count(i)==2:
            #print("%i confirm"%i)
            score=sum(list(filter(lambda n:n!=i,point)))
            #print(score)
            #isconfirm=True
            #print(point)
            return score
            break
    return 0



def judge(matrix,num_of_player,bet):
    for i in range(0,num_of_player):
        print("玩家%i"%i)
        print("%i點"%matrix[i][0])
        #玩家獲勝
        if matrix[i,0]>matrix[0,0]:
            winer=i
            print("玩家%i獲勝"%winer)
            matrix[i,1]+=bet
            matrix[0,1]-=bet
        #玩家落敗
        elif matrix[i,0]<matrix[0,0]:
            print("玩家%i落敗"%winer)
            matrix[i,1]-=bet
            matrix[0,1]+=bet
        #莊家一色通吃
        elif matrix[0,0]==18:
            matrix[1:,1]-=bet
            matrix[0,1]+=bet*num_of_player-1
            print("莊家一色通吃")
        #j玩家一色加倍
        elif matrix[i,0]==18:
            matrix[i,1]+=bet*2
            matrix[0,1]-=bet*2
            print("玩家%i一色加倍"%i)
    print(matrix)  
        

def game_start(matrix,num_of_player):
    for i in range(0,num_of_player):
        matrix[i][0]=roll()
        #print("玩家%i"%i)
        #print("%s分"%matrx[i][0])
    #print(matrix)


# In[ ]:


print ("***擲骰子遊戲***")
win, lose = 0, 0
dice = [i for i in range(1,7)]
num_of_player=int(input("多少玩家:"))
money=int(input("起始金額:"))
#生成num_of_player列的二維list
matrix=np.zeros((num_of_player,2))
matrix[0:,1]=money
bet=int(input("下注金額:"))
game_start(matrix,num_of_player)

while 1:
    judge(matrix,num_of_player,bet)
    play = input('是否繼續(y/n)?')
    if play in ('Y', 'y'):
        bet=int(input("下注金額:"))
        game_start(matrix,num_of_player)
    elif play in ('n', 'N'):
        #print ('目前戰績%s勝%s負' % (win, lose))
        print ('Good Bye!')
        break

