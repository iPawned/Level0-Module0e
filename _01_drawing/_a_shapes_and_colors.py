import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
b = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
b.shape('turtle')
# Set your turtle's speed using .speed(2)
b.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
b.color('green')
b.pencolor('blue')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) or .right(90)

# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
b.begin_fill()
for i in range(4):
    b.forward(100)
    b.right(90)
b.end_fill()
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
b.goto(0, 0)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
b.begin_fill()
b.circle(50, steps=30)
b.end_fill()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
b.begin_fill()
for i in range(4):
    b.forward(100)
    b.right(60)
b.end_fill()
# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
#skibidi toilet
