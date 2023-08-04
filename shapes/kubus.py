#import the turtle modules
import turtle

# Forming the window screen
tut = turtle.Screen()

# Screen position & size (lebar, tinggi, x, y)
tut.setup(500, 400, 850, 200)

# background color green
tut.bgcolor("green")

# window title Turtle
tut.title("KUBUS")

my_pen = turtle.Turtle()

# Draw speed
my_pen.speed(10)

# object color
my_pen.color("orange")

# line size
my_pen.pensize(5)

# forming front square face
for i in range(4):
	my_pen.forward(100)
	my_pen.left(90)

# bottom left side
my_pen.goto(50,50)

# forming back square face
for i in range(4):
	my_pen.forward(100)
	my_pen.left(90)

# bottom right side
my_pen.goto(150,50)
my_pen.goto(100,0)

# top right side
my_pen.goto(100,100)
my_pen.goto(150,150)

# top left side
my_pen.goto(50,150)
my_pen.goto(0,100)

tut.exitonclick()
