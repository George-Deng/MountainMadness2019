def Class_Selection():
     print("We will now ask you questions!")
     Q1 = input("You're party is surrounded by skeleton warriors, what do you do?\
                                A)Retreat and achieve higher ground\n\
                B)Charge!\n\
                C)Support from behind\n\
                D)Hide until an opportunity shows itself")
     Q2 = input("")
     Q3 = input("")
     Q4 = input("")
     Q5 = input("")

def charRace():
    print("Please choose your race: ")
    print("Human, Elf, Dwarf")
    x = input()
    x = x.lower()

    if x == "human":
        print("You chose Human!")
    elif x == "elf":
        print("You chose Elf!")
    else:
        print("You chose Dwarf!")
    Class_Selection()
        

Class_Selection()
print("Welcome to the world of Mountains and caves!")

x = input('Enter your name:')
y = input("Are you sure this is your name(Y/N)")
if y == 'y':
        print("Ok lets move on!")
        charRace()
elif y == 'n':
        while y =='n':
            x = input('Enter your name:')
            y = input("Are you sure this is your name(Y/N)")
            if y == 'y':
                print("Ok lets move on!")
                charRace()

