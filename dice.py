import random


def roll(dicenum, numroll):
    val = 0
    for x in range(numroll):
        val += random.randint(1,dicenum)
        print(val)
    return val

