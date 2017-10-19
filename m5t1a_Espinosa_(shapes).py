# CTI-110
# m5t1a_Espinosa_(shapes)
# Christopher Espinosa
# 10-10-2017
#

import turtle
turtle.shape("turtle")

count = int("2")

while count != 0:
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    count -= 1

turtle.penup()
turtle.forward(200)
turtle.pendown()

count = int("3")
while count != 0:
    turtle.forward(100)
    turtle.left(120)
    count -= 1

turtle.exitonclick()
