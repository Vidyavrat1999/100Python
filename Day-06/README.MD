THIS CODE IS WRITTEN OR REEBORG'S WORLD CHALLENGE GAME

GAME WEBSITE LIKE : https://reeborg.ca/index_en.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not wall_in_front():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move() 
    else:
        turn_left()