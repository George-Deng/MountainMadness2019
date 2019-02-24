import PCUpdated
import MutatedRaccoonNPC
import dice
print("~"*50)
print("You encounter a "+MutatedRaccoonNPC.race+"!")
print("The "+MutatedRaccoonNPC.race+"'s stats are: ")
print("Wisdom: "+str(MutatedRaccoonNPC.wis))
print("Strength: "+str(MutatedRaccoonNPC.strt))
print("Dexterity: "+str(MutatedRaccoonNPC.dex))
print("Constitiution: "+str(MutatedRaccoonNPC.con))
print("Race: "+MutatedRaccoonNPC.race)
print("Class: "+MutatedRaccoonNPC.class1)
print("Weapon: "+MutatedRaccoonNPC.weapon)
turn = 1
counter = 0
while (MutatedRaccoonNPC.hitpoints > 0):
    print("="*22+"Turn:"+str(turn)+"="*22)
    action = input("What would you like to do?: \ntype 'roll' to attack\ntype 'run' to...run\ntype 'spec' to perform a special attack\n")
    if (action == "roll"):
        PCroll=dice.roll(4,2)
        print("You deal: "+str(PCroll)+" damage to your opponent")
        MutatedRaccoonNPC.hitpoints -= PCroll
    elif (action == "run"):
        PCroll=dice.roll(PCUpdated.dex,1)
        if(PCroll > 5):
            print("You succesfully escape")
            print("~"*50)
            break
        else:
            print("You don't escape")
    elif (action == "spec"):
        if(counter == 1):
            print("You've already used your special attack")
            continue
        print("You poke the Mutated Raccoon with a stick!\nRaccoon HP decreased by 2!")
        MutatedRaccoonNPC.hitpoints -= 2
        counter += 1
    if (MutatedRaccoonNPC.hitpoints <= 0):
        print("The opponent is defeated!")
        print("~"*50)
        break
    NPCroll = dice.roll(3,1)
    print("-"*50)
    print("Your opponent deals: "+str(NPCroll)+" damage to you")
    PCUpdated.hitpoints -= NPCroll
    if (PCUpdated.hitpoints <= 0):
        print("You died")
        print("~"*50)
        break
    else:
        print("You have "+str(PCUpdated.hitpoints)+" HP left")
        print("-"*50)
    turn += 1
