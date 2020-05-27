import turtle

turtle.bgcolor('black')

Leo = turtle.Turtle()
Jason = turtle.Turtle()
Alice = turtle.Turtle()
Rene = turtle.Turtle()

Leo.shape('turtle')
Leo.color('red')
Leo.pensize(5)

Alice.shape('square')
Alice.color('yellow')
Alice.pensize(5)

Jason.shape('triangle')
Jason.color('blue')
Jason.pensize(5)

Rene.shape('circle')
Rene.color('green')
Rene.pensize(5)

Leo.setheading(0)
Alice.setheading(90)
Jason.setheading(180)
Rene.setheading(-90)

Leo.forward(200)
Alice.forward(200)
Jason.forward(200)
Rene.forward(200)

sd = 1
for i in range(35):
    Leo.speed(sd)
    Leo.left(70)
    Alice.speed(sd)
    Alice.left(70)
    Jason.speed(sd)
    Jason.left(70)
    Rene.speed(sd)
    Rene.left(70)
    sd = sd + 1  # sd = sd

    Leo.forward(200)
    Alice.forward(200)
    Jason.forward(200)
    Rene.forward(200)

turtle.mainloop()
