import PCUpdated
import BossNPC
import dice

print("~"*50)
print("Welcome to MACM 101! Your professor this semester is Binay!")
print("The "+BossNPC.race+"'s stats are: ")
print("Wisdom: "+str(BossNPC.wis))
print("Strength: "+str(BossNPC.strt))
print("Dexterity: "+str(BossNPC.dex))
print("Constitiution: "+str(BossNPC.con))
print("Race: "+BossNPC.race)
print("Class: "+BossNPC.class1)
print("Weapon: "+BossNPC.weapon)
turn = 1
tries = 3
counter = 0
while (BossNPC.hitpoints > 0):
    print("="*22+"Turn:"+str(turn)+"="*22)
    action = input("What would you like to do?: \ntype 'roll' to attack\ntype 'sleep' to sleep in lecture\ntype 'spec' to perform a special attack\n")
    if (action == "roll"):
        PCroll=dice.roll(4,2)
        print("You deal: "+str(PCroll)+" damage to your opponent")
        BossNPC.hitpoints -= PCroll
    elif (action == "sleep"):
        PCroll=dice.roll(PCUpdated.dex,1)
        if(PCroll > 15):
            print("You succesfully fall asleep")
            print("You lose a chance in the midterm")
            tries -= 1
        else:
            print("You resist the self sabatoge")
    elif (action == "spec"):
        if(counter == 1):
            print("You've already used your special attack")
            continue
        print("You study extra hours!\nYou get an extra chance in the midterm!")
        tries += 1
        counter += 1
    if (BossNPC.hitpoints <= 0):
        print("Binay used his special move: MidTerm1!")
        print("You have: "+str(tries)+" tries")
        while (tries != 0):
            print(("!"*19)+str(tries)+" tries left"+("!"*19))
            print("Solve:((¬p∧p)∨(q∧p))->q")
            answer = input("Enter the answer: ")
            if (answer.lower() == "t" or answer.lower() == "true"):
                print("You passed MACM101! You won!")
                quit()
            tries -= 1
        print("You failed...time to retake it next semsester...")
        break
    NPCroll = dice.roll(8,1)
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

