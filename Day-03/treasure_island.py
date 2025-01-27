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

print("You are at a cross road.↔️ Where do you want to go?")
decision_1 = input('     Type "Left" or "Right"').lower()

if decision_1 == "right":
    print("You fell into a hole.🕳️ Game over!")
elif decision_1 == "left":
    print("You've come to a lake.🏝️ There is an island in the middle of the lake.")
    decision_2 = input('Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if decision_2 == "swim":
        print("You get attacked by an angry trout.🐊 Game over!")
    elif decision_2 == "wait":
        print("You arrived at the island unharmed.😊 There is a house with 3 doors.")
        decision_3 = input("One red, one yellow and one blue. Which color do you choose?").lower()
        if decision_3 == "red":
            print("It's a room full of fire.🔥 Game over!")
        elif decision_3 == "yellow":
            print("You found the treasure.⚱️ You won!")
        elif decision_3 == "blue":
            print("You entered the hell. Game over! 🤪")
        else:
            print("You entered a wrong input. Game over. Play again. 😄")
    else:
        print("You entered a wrong input. Game over. Play again. 😄")
else:
    print("You entered a wrong input. Game over. Play again. 😄")