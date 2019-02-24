import PCUpdated
import RaccoonNPC
import dice

print("You encounter a "+RaccoonNPC.race+"!")
print("The "+RaccoonNPC.race+"'s stats are: ")
print("Wisdom: "+str(RaccoonNPC.wis))
print("Strength: "+str(RaccoonNPC.strt))
print("Dexterity: "+str(RaccoonNPC.dex))
print("Constitiution: "+str(RaccoonNPC.con))
print("Race: "+RaccoonNPC.race)
print("Class: "+RaccoonNPC.class1)
print("Weapon: "+RaccoonNPC.weapon)

while (RaccoonNPC.hitpoints > 0):
    action = input("What would you like to do?: \ntype 'roll' to attack\ntype 'run' to...run\ntype 'spec' to perform a special attack\n")
    counter = 0
    if (action == "roll"):
        PCroll=dice.roll(4,1)
        print("You deal: "+str(PCroll)+" damage to your opponant")
        RaccoonNPC.hitpoints -= PCroll
    elif (action == "run"):
        PCroll=dice.roll(PCUpdated.dex,1)
        if(PCroll > 5):
            print("You succesfully escape")
            break
        else:
            print("You don't escape")
    elif (action == "spec" and counter == 0):
        print("You punch the Raccoon in it's smug little face!\nRaccoon HP decreased by 5!")
        RaccoonNPC.hitpoints -= 5
        counter += counter
if (RaccoonNPC.hitpoints <= 0):
    print("The opponent is defeated!")

