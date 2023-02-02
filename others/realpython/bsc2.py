# Import library
import turtle

# Buat layar
scn = turtle.Screen()
# Warna latar
scn.bgcolor('black')
# (lebar, tinggi, x, y)
scn.setup(500, 500, 1400, 300)
# Ubah Title
turtle.title('basic 2')

# Buat object
t = turtle.Turtle()
# Kecepatan
t.speed(10)
# Warna garis
t.pencolor('white')

turtle.bgcolor('brown')
t.fd(50)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(50)

turtle.bgcolor('grey')
t.penup()
t.goto(50, -50)
t.pendown()
t.circle(50)

turtle.bgcolor('black')
t.penup()
t.goto(-50, -50)
t.pendown()
t.dot(30)

turtle.exitonclick()