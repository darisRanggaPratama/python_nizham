import turtle

t = turtle.Turtle()
# (lebar, tinggi, x, y)
turtle.setup(700, 700, 500, 100)
t.speed(1)
t.screen.bgcolor('#273746')
t.pencolor('#a569bd')

# Pesawat
t.fd(100)
t.right(15)

t.fd(200)
t.left(150)

t.fd(100)
t.right(50)

t.fd(60)
t.right(200)

t.fd(150)



turtle.exitonclick()