import turtle

pen = turtle.Turtle()
pen.speed(0)

pen.penup()
pen.goto(0, -200)
pen.pendown()

pen.setheading(90)
pen.pensize(80)
pen.pencolor('green')


pen.forward(200)
new_pen = pen.clone()

pen.left(65)
new_pen.right(65)
pen.forward(200 * 0.618)
new_pen.forward(200 * 0.618)
pen.hideturtle()
new_pen.hideturtle()

turtle.done()
