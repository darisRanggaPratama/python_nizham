import turtle

# Ukuran Layar
turtle.setup(500, 500, 1030, 300)
# Munculkan Layar
turtle.getscreen()
t1 = turtle.Turtle()
t2 = t1
t1.screen.bgcolor('black')
t1.speed(0)
# Hilangkan panah
t1.hideturtle()

x = int(360/7)
for i in range(x):
    t1.pen(fillcolor='purple', pencolor='purple')
    t1.fd(10)
    t1.lt(17)

t1.penup()
t1.goto(10, 10)
t2.pendown()

y = int(360/7)
for i in range(y):
    t2.pen(fillcolor='orange', pencolor='orange')
    t2.fd(10)
    t2.lt(19)

t2.penup()
t2.goto(150, 150)
t1.pendown()

for i in range(4):
    t1.pen(fillcolor='red', pencolor='red')
    t1.lt(90)
    t1.fd(50)

# Hapus semua garis
#t1.clear()
turtle.exitonclick()
