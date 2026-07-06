# Reeborg Maze Solver
# https://reeborg.ca/
# Algorithm: Right-hand rule

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# The functions below are provided by Reeborg.
# They are included here as placeholders to make this file self-contained.

def turn_left():
    pass


def at_goal():
    pass


def right_is_clear():
    pass


def left_is_clear():
    pass


def move():
    pass


def front_is_clear():
    pass


# Move forward until a wall is reached.
while front_is_clear():
    move()

turn_right()

# If all directions are initially open, the robot may enter an infinite loop.
# Moving to the first wall before starting the algorithm prevents this issue.

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
