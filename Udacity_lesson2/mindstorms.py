import turtle

#square
brad = turtle.Turtle()#Essa é a minha tartaruga
brad.shape("turtle")
brad.color("blue", "black")
brad.speed(7)



def draw_square(brad):
    for i in range(4):
        brad.forward(100)#Direcao para onde ela vai
        brad.right(90)



def draw_circle():

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(90)


def draw_triangle():

    lizzie = turtle.Turtle()
    lizzie.shape("circle")
    lizzie.color("black")

    lizzie.forward(160)
    lizzie.left(110)
    lizzie.forward(150)
    lizzie.left(123)
    lizzie.forward(169)


def screen():

    window = turtle.Screen()#Defino aqui a tela
    window.bgcolor("red")# Defino aqui a cor da tela

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

        
    #draw_circle()
    #draw_triangle()

    window.exitonclick()


screen()