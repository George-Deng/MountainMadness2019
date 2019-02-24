import sys
import time
import random
import PCUpdated
import RaccoonNPC
import dice
import BossNPC
import MutatedRaccoonNPC

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

print_slow("Type whatever you want here\n")


def Class_Selection():
     print("We will now ask you questions to determine your class!")
     Q1 = ""
     Q2 = ""
     Q3 = ""
     Q4 = ""
     Q5 = ""
     while ((Q1 != "A") and (Q1 !="B") and (Q1 !="C") and (Q1 !="D")):
         Q1 = input("you're at a house party, Where are you?\n\
                    A)In the corner drinking alone\n\
                    B)Mixing drinks\n\
                    C)Dancing in the middle of a circle\n\
                    D)Playing darts\n\
                    ")
     while ((Q2 != "A") and (Q2 !="B") and (Q2 !="C") and (Q2 !="D")):
         Q2 = input("Where do you sit in a class?\n\
                    A)In the back\n\
                    B)In the middle\n\
                    C)Im a nerd!\n\
                    D)I dont go to class\n\
                    ")
     while ((Q3 != "A") and (Q3 !="B") and (Q3 !="C") and (Q3 !="D")):
         Q3 = input("Whats your favorite activity?\n\
                    A)Learning something new\n\
                    B)Playing with animals\n\
                    C)Competitive sports!\n\
                    D)Sleep...\n\
                    ")
     while ((Q4 != "A") and (Q4 !="B") and (Q4 !="C") and (Q4 !="D")):
         Q4 = input("How well do you work with others\n\
                    A)Competting against others\n\
                    B)I lead!\n\
                    C)I have no friends\n\
                    D)I'm a follower\n\
                    ")
     while ((Q5 != "A") and (Q5 !="B") and (Q5 !="C") and (Q5 !="D")):
         Q5 = input("Your party is surrounded by skeleton warriors, what do you do?\n\
                    A)Retreat and achieve higher ground\n\
                    B)Charge!\n\
                    C)Support from behind\n\
                    D)Hide until an opportunity shows itself\n\
                    ")
         if (Q5 == "D"):
            class1 = "Rogue"
            print("Your class is: ", class1)
         elif (Q5 == "C"):
            class1 = "Mage"
            print("Your class is: ", class1)
         elif (Q5 == "B"):
            class1 = "Warrior"
            print("Your class is: ", class1)
         elif (Q5 == "A"):
            class1 = "Ranger"
            print("Your class is: ", class1)


         
    

def charRace():
    print("Please choose your race: Human, Elf, or Dwarf\n")
    print("If you choose Human, all stats (wisdom, strength, dexterity and constitution) will +1.")
    print("If you choose Elf, wisdom and dexterity will +2.")
    print("If you choose Dwarf, constitution and strength will +2.\n")

    boolean = True
    while boolean == True:
        x = input("Choose your race: ")
        x = x.lower()        
        if x == "human":
            output = "You chose Human!"
            print(output)
            boolean = False
        elif x == "elf":
            output = "You chose Elf!"
            print(output)
            boolean = False
        elif x == "dwarf":
            output = "You chose Dwarf!"
            print(output)
            boolean = False
        else:
            print("Please enter a valid input.")

    
    Class_Selection()

print("Welcome to the world of Mountains and Caves!")

name = input('Enter your name: ')
name = name.upper()
y = input("Are you sure this is your name(Y/N)")
if y == 'y':
        print("Ok lets move on!")
        charRace()
elif y == 'n':
        while y =='n':
            x = input('Enter your name: ')
            y = input("Are you sure this is your name(Y/N)")
            if y == 'y':
                print("Ok lets move on!")
                charRace()
print('Your adventure begins with the soothing sound of your mom screaming " WAKE UP', name, '", ')
print('You shoot out of your bed realizing you have an exam today')
print('Before even realizing it you were already out of bed and quickly changing to catch the bus')
print('Unfortunately for you the 145 left before you could catch it! And there’s a sea of students in line for the next bus!')
print('But then… An idea pops into your head! Why not fight through the creatures of the SFU mountain to rise to the top!')
print('You begin walking up the hills but run into your first monster!')
print('Grab your weapon and prepare for battle!')
##Racoon fight
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
        PCroll=dice.roll(4,2)
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
PCUpdated.hitpoints = 18
##Racoon fight ended



print('You continue on your harsh journey up the mountain, but alas you run into your first obstacle!')
print('Your going to have to take a detour!')
print('You see one path leading upwards that might lead to a group of mutated racoons!(Path A)')
print('The other path leads down back the mountain where you started!(Path B)')
path1 = input('Which path will you chose?(A or B)')
if path1 == 'A':
    print('You decided to lead your life bravely and go down the path of mutated racoons!')
    ##Mutated Racoon fight
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
        PCUpdated.hitpoints = 18
    ##Mutated Racoon fight End
else:
    print('You are a coward and the racoons can smell your cowardness and come eat you!')
    print('Gameover!')
    sys.exit()

print('Once you make your way through the racoons, you continue your expedition to the top of SFU.')
print('After what felt like hours fighting through the snow, you finally make it to the convocation mall!')
print('you encounter 3 different paths; left, right or center')
for x in range (3):
    maze1 = input('Will you turn Left, Right or Center?(L or R or C): ')
    if maze1 == 'R':
        print('Sadly your greatest fear has come true!')
        print('The SFU construction team is blocking your way!')
        print('You must find another path!')
        print('Time is of the essence, you must hurry!')
    elif maze1 == 'L':
        print('Sadly your greatest fear has come true!')
        print('The SFU construction team is blocking your way!')
        print('You must find another path!')
        print('Time is of the essence, you must hurry!')
    elif maze1 == 'C':
        print('Sadly your greatest fear has come true!')
        print('The SFU construction team is blocking your way!')
        print('You must find another path!')
        print('Time is of the essence, you must hurry!')


print('Once you tried all 3 paths, you realize there is another path...')
print('You quickly rush over to it and find your way to your class')
##boss fight
print("!"*50)
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

