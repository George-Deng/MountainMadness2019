import random

def CharStats():
    print("Stat Rolls using 4 six sided die")
    stats = [0,0,0,0]
    for i in range(4):
        stats[i] = random.randint(0,6) + random.randint(0,6) + random.randint(0,6) + random.randint(0,6)
    return stats
print(CharStats())
