import turtle

t = turtle.Turtle()
# (lebar, tinggi, x, y)
turtle.setup(500, 500, 1030, 300)
# Kecepatan
t.speed(0)
t.screen.bgcolor('black')
t.pen(fillcolor='purple', pencolor='purple')

x = 11
t.begin_fill()
for i in range(x):
    h = t.heading()
    # (radius, panjang)
    t.circle(100, 60)
    t.lt(120)
    t.circle(100, 60)
    t.setheading(h)
    t.lt(360/x)
    
t.end_fill()


# hilangkan panah
t.hideturtle()
# Stop garis
t.penup()
# Koordinat
t.goto(0, -30)
t.showturtle()
# Mulai garis
t.pendown()
t.pen(fillcolor='orange', pencolor='orange')
t.begin_fill()
t.circle(30)
t.end_fill()

t.hideturtle()
t.penup()
t.goto(0, -20)
t.showturtle()
t.pendown()
t.pen(fillcolor='blue', pencolor='blue')
t.begin_fill()
t.circle(20)
t.end_fill()
t.hideturtle()

# menit 6

turtle.exitonclick()
