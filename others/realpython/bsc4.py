# Import library
import turtle

# Buat layar
scn = turtle.Screen()
# Warna latar
scn.bgcolor('black')
# (lebar, tinggi, x, y)
scn.setup(500, 500, 1400, 300)
# Ubah Title
turtle.title('basic 4')

# Buat object
t = turtle.Turtle()
# Kecepatan
t.speed(1)
# Warna garis
t.pencolor('white')

t.pensize(5)
t.fd(100)

t.penup()
t.goto(-50, 100)
t.pendown()
t.shapesize(3, 3, 3)
t.fillcolor('orange')
t.fd(50)
t.pencolor('green')
t.rt(15)
t.fd(50)

t.color('pink', 'blue')




turtle.exitonclick()