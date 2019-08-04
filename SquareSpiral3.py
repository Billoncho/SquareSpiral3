# SquireSpiral3.py
# Billy Ridgeway
# Creates a square spiral that rotates slightly as it's
# being drawn and uses a blue pen.

import turtle           # Imports the turtle graphics library.
t = turtle.Pen()        # Creates a new turtle called t.
t.speed(0)              # Sets the pen's speed to fast.
t.pencolor("blue")      # Sets the pen's color to blue.

# Creates a for loop.
for x in range (100):   # Set the range of x to 100.
    t.forward(2*x)      # Moves the pen forward 2 times the value of x.
    t.left(91)          # Turns the pen left by 91 degrees.
