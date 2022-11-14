# Treasure Island
# printing Treasure Icon
print('''

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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
# Welcoming
print("Welcome to Treasure Island!")
print("Ur mission is to find the treasure")
# getting left or right
first = input("Where do u want to go. 'left' or 'right'")
if first.lower() == "left":
    print("u fell into a manhole. \n Game Over")
else:
    # getting swim or wait
    second = input("There is a ocean in front of u. Do u want to 'swim' or 'wait' for the boat")
    if second.lower() == "swim":
        print(" There is a big storm coming. \n Game Over")
    else:
        # getting red, green or blue door
        door = input("There are three doors, each in red, green and blue. Which door do u want to open")
        if door.lower() == "green":
            print("Hurrah! U find the Treasure. You Win")
        elif door.lower() == "red":
            print("There was a lion behind the door. \n Game Over")
        elif door.lower() == "blue":
            print("There was a cheetah behind the door. \n Game Over")
