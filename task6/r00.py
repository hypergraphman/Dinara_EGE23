from turtle import *

shape('square')
shapesize(0.1)

cell = 20
left(90)

for i in range(7):
    forward(10 * cell)
    right(120)

penup()
goto(0, 0)
for x in range(0, (10 + 1) * cell, cell):
    for y in range(0, (10 + 1) * cell, cell):
        goto(x, y)
        stamp()

done()