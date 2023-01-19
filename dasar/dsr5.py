import turtle

turtle.setup(500, 500, 1030, 300)
turtle.getscreen()
turtle.speed(0)

t = turtle.Turtle()

for x in range(4):
    t.fd(50)
    t.rt(90)
    
t.penup()
t.fd(100)
t.pendown()

t.circle(25)

t.penup()
t.bk(200)
t.pendown()

t.circle(50, steps=3)

t.penup()
t.goto(25, 25)
t.pendown()

t.circle(50, steps=4)

t.penup()
t.goto(-55, -55)
t.pendown()

t.dot(25)
t.fd(55)
t.dot(25)
t.lt(15)
t.fd(65)
t.dot(35)
    
turtle.exitonclick()