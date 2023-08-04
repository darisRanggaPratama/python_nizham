from turtle import *
import colorsys

setup(700, 800, 650, 0)
title("leavesFlower")
speed(0)

bgcolor("black")
h = 0

for x in range(16):
    for y in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        rt(90)
        circle( 150 - y * 6, 90)
        lt(90)
        circle(150 - y * 6, 90)
        rt(180)
    circle(40, 24)

hideturtle()
exitonclick()