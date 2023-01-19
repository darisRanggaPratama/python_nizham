import turtle

t = turtle.Turtle()
# (lebar, tinggi, x, y)
turtle.setup(500, 500, 1030, 300)
t.speed(10)
t.screen.bgcolor('#273746')
t.pencolor('#a569bd')

# Kotak
for i in range(4):
    t.pencolor('#e59866')
    t.fd(100)
    t.lt(90)


# Segitiga
for i in range(3):
    t.pencolor('#82e0aa')
    t.fd(120)
    t.lt(120)


# Lingkaran
t.pencolor('#f1948a')
t.circle(100)

turtle.exitonclick()
