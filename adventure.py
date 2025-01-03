#ACL ADVENTURE

clothing = {"tops": ["black aritzia bodysuit", "vintage lingerie top", "band t-shirt", "neon green bikini top", "shrek costume"],
    "bottoms" : ["baggy blue jeans", "long flowy white indie skirt", "black micro skirt", "itty bitty denim skirt"],
    "accessories": ["sunglasses", "chunky metal belt", "red fanny pack", "hello kitty ears"],
    "shoes":["cowboy boots", "leather flip flops", "chunky heels", "frat shoes", "ballet pointe shoes"]}

food = {"food": ["nachos", "pizza", "tacos", "filet mignon", "chicken tenders"],
        "drinks": ["soda", "water", "lemonade", "beer", "iced tea"]}

artists1 = {"afternoon": ["Leon Bridges", "Stephen Sanchez"],
            "night": ["Chris Stapleton", "Blink-182", "Fletcher"]}

artists2 = {"afternoon": ["Say She She", "Jon Muq", "Benson Boone"],
            "night": ["Dua Lipa", "Renee Rapp", "Silent Disco"]}

artists3 = {"afternoon": ["Sturgill Simpson", "Flo", "David Shaws"],
            "night": ["Tyler, the Creator", "Chappell Roan", "Kehlani", "Dom Dolla"]}

def intro():
    name = input("Hi! What's your name? ")
    print()
    print("Hello", name, "! Welcome to Austin City Limits 2024! Are you ready to go to ACL day 1?")
    answer = input("Enter yes or no: ")
    if answer == "no":
        print("Okay bye! You're a loser and didn't even make it to day 1")
    elif answer == "yes":
      print()
      print("Okay let's go!")
      dayOne()
    else:
        print("That wasn't an option...")

def generator(dict):
    output = []
    for key, value in dict.items():
        print()
        print(f"{key}: {', '.join(value)}")
        item = input("Choose an item: ")
        while item not in value:
            print()
            print("That item isn't an option.")
            item = input("Choose an item: ")
        output.append(item)
    return output


def dayOne():
    print("Let's pick your outfit first! Here are the list of tops, bottoms, accessories, and shoes in your closet. Choose one of each!")
    dayOneOutfit = generator(clothing)
    print()
    ride = input("Time to head out! Would you like to take the bus or an uber? ")
    print()
    print("You've arrived at ACL! Let's pick your artists for the day.")
    print()
    dayOneArtists = generator(artists1)

    if ride == "bus":
      print("The bus was delayed and you arrived late, so you missed ", dayOneArtists[0], ". Luckily you saved money so you can get some food now.")
      print()
      dayOneFood = generator(food)
    else:
      print("You got to ACL with plenty of time to spare! Enjoy your first artist, ", dayOneArtists[0])
      print()
      print("Now pick what food you want!")
      print()
      dayOneFood = generator(food)

    if "tacos" in dayOneFood:
      print("You got food poisoning from the tacos you ate. Yikes... You had to leave early so you're going to miss ", dayOneArtists[1])
      print()
      answer = input("Would you like to move to Day Two of ACL? ")
      if answer == "yes":
        dayTwo()
      else:
        "Goodbye!"
        return
    else:
      print("Hope you enjoy your", dayOneFood[0], "and", dayOneFood[1])
      print()
      print("Now time for", dayOneArtists[1])
      print()
      print("Hope you had a great day at ACL!")
      print()
      answer = input("Would you like to move to Day Two of ACL? ")
      if answer == "yes":
        dayTwo()
      else:
        "Goodbye!"
        return


def dayTwo():
    print("Welcome to Day Two!")
    print()
    print("Let's pick your outfit first! Here are the list of tops, bottoms, accessories, and shoes in your closet. Choose one of each!")
    print()
    dayTwoOutfit = generator(clothing)
    dayTwoArtists = generator(artists2)
    ride = input("Time to head out! Would you like to take the bus or an uber? ")
    print()
    print("You've arrived at ACL! Let's pick your artists for the day.")
    print()
    if ride == "bus":
      print("The bus was delayed and you arrived late, so you missed ", dayTwoArtists[0], ". Luckily you saved money so you can get some food now.")
      print()
    else:
      print("You got to ACL with plenty of time to spare! Enjoy your first artist, ", dayTwoArtists[0])
      print()
    if "shrek costume" in dayTwoOutfit:
        print("Aw shucks. You unfortunately suffered from heat exhaustion in your shrek costume. Turns out there was no ventilation. You had to get ambulanced out.")
        return
    if "ballet pointe shoes" or "leather flip flops" in dayTwoOutfit:
        print("You actually got ringworm from wearing shoes that are not yours. That's what you get for putting your feet in places it does not belong. People with hazmat suits escorted you out.")
        return
    print("Pick what food you would like to order!")
    print()
    dayTwoFood = generator(food)
    print("Hope you enjoy your", dayTwoFood[0], "and", dayTwoFood[1])
    print()
    print("Hope you had a great day at ACL!")
    print()
    answer = input("Would you like to move to Day Three of ACL?")
    print()
    if answer == "yes":
      dayThree()
    else:
      "Goodbye!"
      return

def dayThree():
    print("Welcome to Day Three!")
    print()
    print("Let's pick your outfit first! Here are the list of tops, bottoms, accessories, and shoes in your closet. Choose one of each!")
    print()
    dayThreeOutfit = generator(clothing)
    if "hello kitty ears" in dayThreeOutfit:
      print("Oh no! Your hello kitty ears have been stolen! You found the culprit and started beating him up. But unfortunately he was stronger than you. The paramedics had to escort you home.")
      return
    if "chunky metal belt" in dayThreeOutfit:
      print("Your chunky metal belt hit the taser of the security guard. You tased him. They kicked out for disorderly conduct.")
      return
    print("Pick what food you would like to order!")
    print()
    dayThreeFood = generator(food)
    print("Hope you enjoy your", dayThreeFood[0], "and", dayThreeFood[1])
    print()
    print("You made it out alive! Congratulations, you made it out of ACL despite many harships. You are a fighter, or maybe you're just lucky")


def main():
    intro()

main()
