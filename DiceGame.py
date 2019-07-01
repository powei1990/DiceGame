import random

def roll():
    result=[]
    for i in range(4):
        result.append(random.randrange(1, 7))
    check(result)
    return result

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


banker=roll()
player=roll()

