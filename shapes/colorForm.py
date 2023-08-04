from turtle import *
import colorsys as cs

setup(700, 800, 650, 0)
tracer(10)
width(4)
bgcolor("black")
speed(10)

def square(x):
    for i in range(3):
        fd(x)
        lt(90)
    fd(x)
    
for a in range(20):
    for b in range(10):
        color(cs.hsv_to_rgb(b/10, 1-a/20, 1))
        rt(135)
        square(200-a*4)
        rt(135)
        circle(50, 36)

hideturtle()

exitonclick() 

done()       