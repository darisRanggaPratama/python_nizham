import turtle

t = turtle.Turtle()
# (lebar, tinggi, x, y)
turtle.setup(500, 500, 1030, 300)
t.speed(0)
t.screen.bgcolor('#273746')
t.pencolor('#a569bd')

x = 30
for i in range(x):
    h = t.heading()
    # (radius, panjang)
    t.circle(100, 60)
    t.lt(120)
    t.circle(100, 60)
    t.setheading(h)
    t.lt(360/x)


# hilangkan panah
t.hideturtle()
t.penup()
# Koordinat
t.goto(0, -30)
t.showturtle()
t.pendown()
t.circle(30)

# hilangkan panah
t.hideturtle()
t.penup()
t.goto(0, -20)
t.showturtle()
t.pendown()
t.circle(20)

# menit 6





turtle.exitonclick()
