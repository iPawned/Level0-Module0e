import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def get_next_color(i):
    return colors[i % len(colors)]


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('black')
    window.setup(width=0.75, height=0.9, startx=0, starty=0)
    
    colors = ('red', 'blue', 'green', 'yellow', 'orange')
    
    # Make a new turtle
    gg = turtle.Turtle()
    # Make the turtle shape 'turtle', .shape('turtle')
    gg.shape('turtle')
    # Set the turtle speed to max (0)
    gg.speed(0)
    # Set the turtle width to 1
    gg.width(1)
    # Create a variable to hold the number of sides in a pentagon
    sides =4
    # Create a variable to be the angle of 360 divided by the sides variable
    angle = 360/sides
    # Use a for loop to repeat ALL the following lines of code 360 times. 
    for i in range(2000):
        if i == 100:
            gg.width(2)
        if i == 200:
            gg.width(3)
        if 1 == 300:
            gg.width(4)
        if i == 400:
            gg.width(5)
        if i == 500:
            gg.width(6)
        if i == 600:
            gg.width(7)
        if i == 700:
            gg.width(8)
        if i == 700:
            gg.width(9)
        if i == 800:
            gg.width(10)
        if i == 900:
            gg.width(11)
        if i == 1000:
            gg.width(12)
        if i == 1100:
            gg.width(13)
        if i == 1200:
            gg.width(14)
        if i == 1300:
            gg.width(15)
        if i == 1400:
            gg.width(16)
        gg.pencolor(get_next_color(i))
        gg.forward(i)
        gg.right(angle+1)
        # If the loop variable (i) is equal to 100, set the turtle width to 2
        
        # If the loop variable (i) is equal to 200, set the turtle width to 3
        
        # Use the get_next_color function to set the turtle pencolor,
        # *hint .pencolor(get_next_color(i))
        
        # Move the turtle forward by the loop variable, *hint .forward(i)
        
        # Turn the turtle to the right by the angle variable + 1

    # Hide your turtle so you can see the pattern.
        
    # Check the pattern against the picture in the recipe. If it matches, you are done!
    
    # Variations:
    # *Make the pattern really huge
    # *Change the colors
    # *Experiment with different shapes
    
    # Call the turtle.done() method
    turtle.done()
