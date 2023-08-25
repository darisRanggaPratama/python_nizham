# Bendera Indonesia 🇮🇩
from turtle import *
# (lebar, tinggi, x, y)
setup(700, 500, 600, 100)
fillcolor('red')
begin_fill()
for i in range(9):
    forward(300) if i % 2 == 0 else forward(100) 
    right(90)
    if i == 4: 
        end_fill() 
        fillcolor('white') 
        begin_fill() 
        goto(300, -100)
end_fill() 
exitonclick()
