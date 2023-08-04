# import package
import turtle

# Forming the window screen
tut = turtle.Screen()

# Screen position & size (lebar, tinggi, x, y)
tut.setup(500, 400, 850, 200)

pen = turtle.Turtle()
pen.speed(10)

# method to raw pattern
# of circle with rad radius
def draw(rad):
	
	# draw circle
	pen.circle(rad)
	
	# set the position by using setpos()
	pen.up()
	pen.setpos(0,-rad)
	pen.down()

# loop for pattern
for i in range(5):
	draw(20+20*i)

tut.exitonclick()