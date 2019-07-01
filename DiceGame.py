#!/usr/bin/env python
# coding: utf-8

# In[72]:


import random
banker=roll()
player=roll()
#print("banker")
#print(banker)
#print("player")
#print(player)


# In[68]:


def roll():
    result=[]
    for i in range(4):
        result.append(random.randrange(1, 7))
    check(result)
    return result


# In[65]:


def check(result):
    for i in range(6):
        if result.count(i)==2:
            print("%i confirm"%i)
            isconfirm=True
            print(result)

           #calculate(result,i)
            break
        else:
            isconfirm=False
    if isconfirm==False:
        print("reroll")
        roll()


# In[2]:


def calculate(result,i):
    temp[0:4]=result[0:4] 
    temp.remove(i)
    temp.remove(i)
        


# In[73]:


player


# In[ ]:




