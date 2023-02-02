# Import library
import turtle

# Buat layar
scn = turtle.Screen()
# Warna latar
scn.bgcolor('black')
# (lebar, tinggi, x, y)
scn.setup(500, 500, 1400, 300)
# Ubah Title
turtle.title('basic 3')

# Buat object
t = turtle.Turtle()
# Kecepatan
t.speed(1)
# Warna garis
t.pencolor('white')

for i in range(10):
    t.shapesize(1, 5, 10)
    t.shapesize(10, 5, 1)
    t.shapesize(1, 10, 5)
    t.shapesize(10, 1, 5)




turtle.exitonclick()