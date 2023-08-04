import turtle as t
import colorsys as c


t.setup(700, 800, 650, 0)
t.title("ColorFlower")
t.speed(0)
t.tracer(10)
t.width(2)
t.bgcolor("black")

for a in range(25):
    for b in range(15):
        t.color(c.hsv_to_rgb(b/15, a/25, 1))
        t.rt(90)
        t.circle(200-a*4, 90)
        t.lt(90)
        t.circle(200-a*4, 90)
        t.rt(180)
        t.circle(50, 24)

t.hideturtle()
t.exitonclick()
