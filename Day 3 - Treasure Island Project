print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction_choice = input(
    "You are in a dungeon, crawling through the dark you come across a fork in your path. Which way do you go?\nType: \"Left\" or \"Right?\" ").lower()
if direction_choice == "right":
    print(
        "As you go through the passage on the right, you step over what feels like loose stone tiles. With another step, you fall through the floor.\nGame Over")
elif direction_choice == "left":

    river_choice = input(
        "You make it through the fork in the pathway, to find an underground river. How do you proceed? Swim through it, or explore the surroundings?\nType: \"Swim\" or \"Explore\" ").lower()
    if river_choice == "swim":
        print(
            "As you attempt to cross the river a realisation dawns upon you; you overestimated your swimming ability and underestimated the river's current.\nGame over")
    elif river_choice == "explore":
        print(
            "You explore your surroundings. Thanks to your keen eye, you notice a hidden switch in the wall.\nAs you press the switch, a bridge emerges from under the river, creating a safe path.")

        door_choice = input(
            "You pass the river and enter a corridor. At the end of it you come across 3 doors; Red, Yellow, and Blue.\nWhich door do you open?\nType: \"Red\" or \"Yellow\" or \"Blue\" ").lower()
        if door_choice == "red":
            print(
                "As you open the Red door, hellfire spews from within the cracks. You are engulfed in flames.\nGame over")
        elif door_choice == "blue":
            print(
                "As you open the Blue door, a swarm of bees flies out and surrounds you.\nGame Over")
        elif door_choice == "yellow":
            print(
                "As you pry the door open, you unveil the treasure you were seeking.\nCongratulations, you have won!!!")
        else:
            print("Your decision didn't make any sense.\nGame over")
