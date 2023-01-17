import turtle

t = turtle.Turtle()
# (lebar, tinggi, x, y)
turtle.setup(500, 500, 1030, 300)
t.screen.bgcolor('black')

t.pencolor('red')
t.speed(1)
# fd: forward = maju
t.fd(100)
t.lt(80)
t.fd(200)
t.rt(90)
t.fd(100)

turtle.done()
