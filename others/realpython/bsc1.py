# import library
import turtle

# Buat layar
scn = turtle.Screen()
# Warna latar
scn.bgcolor('black')
# (lebar, tinggi, x, y)
scn.setup(500, 500, 1400, 300)

# Buat object
t = turtle.Turtle()
# Kecepatan
t.speed(1)
# Warna garis
t.pencolor('white')

t.rt(90)
t.fd(100)
t.lt(90)
t.bk(100)

t.penup()
t.goto(100,100)
t.pendown()
t.home()


turtle.exitonclick()