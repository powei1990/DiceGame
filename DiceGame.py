#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


# In[ ]:


def roll():
    score = 0
    while not score:
        point=[random.choice(dice) for a in range(4)]
        print(point)
        score=check(point)
        #print(score)
    return score


# In[ ]:


def check(point):
    for i in range(6):
        if point.count(i)==6:
            score=18
            isconfirm=True
            return score
        elif point.count(i)==2:
            #print("%i confirm"%i)
            score=sum(list(filter(lambda n:n!=i,point)))
            #print(score)
            isconfirm=True
            #print(point)
            return score
            break
    return 0


# In[ ]:


def compare(matrx):
    
        


# In[ ]:


def endgame():


# In[ ]:


def game_start(matrx,num_of_player):
    for i in range(0,num_of_player):
        matrx[i][0]=roll()
        print("玩家%i"%i)
        print("%s分"%matrx[i][0])
    #print(matrx)


# In[ ]:


print ("***擲骰子遊戲***")
dice = [i for i in range(1,7)]
num_of_player=int(input("多少玩家"))
#生成num_of_player列的二維list
matrx=[[0 for i in range(3)] for j in range(num_of_player)]
#print(matrx)
game_start(matrx,num_of_player)


# In[ ]:





# In[ ]:




