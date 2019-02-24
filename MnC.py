def Class_Selection():
     print("We will now ask you questions!")
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

print("Welcome to the world of Mountains and caves!")

x = input('Enter your name: ')
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

