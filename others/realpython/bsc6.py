# Import library
import turtle

# Buat layar
scn = turtle.Screen()
# Warna latar
scn.bgcolor('black')
# (lebar, tinggi, x, y)
scn.setup(500, 500, 1400, 300)
# Ubah Title
turtle.title('basic 6')

# Buat object
t = turtle.Turtle()
# Kecepatan
t.speed(0)
# Warna garis
t.pencolor('red')

n = 10
while n <= 400:    
    t.fd(n)
    t.rt(120)
    n = n + 10
    
t.clear()
t.penup()
t.home()
t.pendown()

u = t.clone()
m = 10
while m <= 400:    
    u.fd(m)
    u.rt(90)
    m = m + 10








turtle.exitonclick()