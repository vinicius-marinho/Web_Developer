import turtle

window = turtle.Screen()
window.bgcolor("white")


inicials = turtle.Turtle()
inicials.color("blue")


def first():
    inicials.left(110)
    inicials.forward(150)
    inicials.back(150)
    inicials.right(40)
    inicials.forward(150)


inicials_2 = turtle.Turtle()
inicials_2.color("blue")



def second():
    inicials_2.penup()
    inicials_2.goto(30,0)
    inicials_2.forward(100)
    inicials_2.pendown()
    inicials_2.left(90)
    inicials_2.forward(140)
    inicials_2.right(140)
    inicials_2.forward(100)
    inicials_2.left(97.5)
    inicials_2.forward(98)
    inicials_2.right(137)
    inicials_2.forward(138)

first()
second()


window.exitonclick()