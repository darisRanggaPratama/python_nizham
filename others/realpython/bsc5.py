# Import library
import turtle

# Buat layar
scn = turtle.Screen()
# Warna latar
scn.bgcolor('black')
# (lebar, tinggi, x, y)
scn.setup(500, 500, 1400, 300)
# Ubah Title
turtle.title('basic 5')

# Buat object
t = turtle.Turtle()
# Kecepatan
t.speed(1)
# Warna garis
t.pencolor('red')

t.fillcolor('blue')
t.begin_fill()

for i in range(3):
   
    t.rt(120)
    t.fd(100)    

t.end_fill()

u = t.clone()

for i in range(10):
    t.clear()
    t.shape('turtle')
    t.goto(100, 100)
    u.shape('arrow')
    t.goto(-100, 100)
    t.shape('circle')
    t.goto(-100, -100)
    u.shape('square')
    t.goto(100, -100)
    t.shape('triangle')
    t.goto(100, -100)
    u.shape('classic')
    t.home()






turtle.exitonclick()