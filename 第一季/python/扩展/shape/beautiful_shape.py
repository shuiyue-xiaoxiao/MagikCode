import turtle

def draw_square(some_turtle):

    for i in range (1, 5):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("gold")
    #Turtle Brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(0)
    brad.pensize(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #Turtle Angie
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue")
    angie.speed(0)
    angie.pensize(2)
    size=1
    for i in range(1, 301):
        angie.forward(size)
        angie.right(91)
        size = size + 1

    window.exitonclick()

draw_art()
