import PCUpdated
import RaccoonNPC
import dice
print("~"*50)
print("You encounter a "+RaccoonNPC.race+"!")
print("The "+RaccoonNPC.race+"'s stats are: ")
print("Wisdom: "+str(RaccoonNPC.wis))
print("Strength: "+str(RaccoonNPC.strt))
print("Dexterity: "+str(RaccoonNPC.dex))
print("Constitiution: "+str(RaccoonNPC.con))
print("Race: "+RaccoonNPC.race)
print("Class: "+RaccoonNPC.class1)
print("Weapon: "+RaccoonNPC.weapon)
turn = 1
counter = 0
while (RaccoonNPC.hitpoints > 0):
    print("="*22+"Turn:"+str(turn)+"="*22)
    action = input("What would you like to do?: \ntype 'roll' to attack\ntype 'run' to...run\ntype 'spec' to perform a special attack\n")
    if (action == "roll"):
        PCroll=dice.roll(4,1)
        print("You deal: "+str(PCroll)+" damage to your opponent")
        RaccoonNPC.hitpoints -= PCroll
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
        print("You punch the Raccoon in it's smug little face!\nRaccoon HP decreased by 5!")
        RaccoonNPC.hitpoints -= 5
        counter += 1
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

if (RaccoonNPC.hitpoints <= 0):
    print("The opponent is defeated!")
    print("~"*50)






