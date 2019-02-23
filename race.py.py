def charRace():
    print("Please choose your race: ")
    print("Human, Elf, Dwarf")

    boolean = True
    while boolean == True:
        x = input()
        x = x.lower()
        
        if x == "human":
            print("You chose Human!")
            boolean = False
        elif x == "elf":
            print("You chose Elf!")
            boolean = False
        elif x == "dwarf":
            print("You chose Dwarf!")
            boolean = False
        else:
            print("Please enter a valid input.")

charRace()
