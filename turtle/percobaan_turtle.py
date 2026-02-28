import turtle
import math

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("3D Heart")
screen.bgcolor("black")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)  # Maximum speed for turtle
pen.hideturtle()

# Function to draw the heart
def gambar_hati():
    pen.penup()
    for z in range(0, 150):  # Layering effect for 3D
        pen.goto(0, 0)
        pen.pendown()
        
        # Gradient color
        r = int(255 - z * 1.5)
        g = int(100 + z * 0.5)
        b = int(z)
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        pen.color(r, g, b)

        # Begin drawing the heart shape
        pen.begin_fill()
        for angle in range(0, 360, 2):
            radians = math.radians(angle)
            x = (16 * math.sin(radians) ** 3)
            y = -(13 * math.cos(radians) - 5 * math.cos(2 * radians) - 2 * math.cos(3 * radians) - math.cos(4 * radians))
            pen.goto(x * (z * 0.02 + 1) * 15, y * 15)
        pen.end_fill()
        pen.penup()

# Set color mode to 255 (RGB)
turtle.colormode(255)

# Draw the 3D heart
gambar_hati()

# Keep the window open
screen.mainloop()
