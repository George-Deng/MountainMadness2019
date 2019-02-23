def charRace():
    print("Please choose your race: Human, Elf, or Dwarf\n")
    print("If you choose Human, all stats (wisdom, strength, dexterity and constitution) will +1.")
    print("If you choose Elf, wisdom and dexterity will +2.")
    print("If you choose Dwarf, constitution and strength will +2.\n")

    boolean = True
    while boolean == True:
        x = input()
        x = x.lower()        
        if x == "human":
            output = "You chose Human!"
            boolean = False
        elif x == "elf":
            output = "You chose Elf!"
            boolean = False
        elif x == "dwarf":
            output = "You chose Dwarf!"
            boolean = False
        else:
            print("Please enter a valid input.")

    return output

