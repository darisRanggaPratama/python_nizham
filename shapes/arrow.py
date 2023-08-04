# import package
import turtle

# Forming the window screen
tut = turtle.Screen()

# Screen position & size (lebar, tinggi, x, y)
tut.setup(500, 400, 850, 200)

pen = turtle.Turtle()

pen.speed(10)

# forward turtle by 100
pen.forward(100)

# stamp the turtle shape
pen.stamp()

# set the position by using setpos()
pen.up()
pen.setpos(-50,50)
pen.down()

# forward turtle by 100
pen.forward(100)

# stamp the turtle shape
pen.stamp()

# set the position by using goto()
pen.up()
pen.goto(-50,-50)
pen.down()

# forward turtle by 100
pen.forward(100)

tut.exitonclick()
