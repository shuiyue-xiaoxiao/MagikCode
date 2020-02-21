import turtle 

wn = turtle.Screen() 
alex = turtle.Turtle() 


def drawRect(): 
    alex.speed(0) 
    alex.up() 
    alex.fillcolor("green") 
    alex.begin_fill() 
    alex.setpos(-250, -100) 
    alex.down() 
    for i in range(2): 
     alex.forward(500) 
     alex.left(90) 
     alex.forward(300) 
     alex.left(90) 
    alex.end_fill() 
drawRect() 

def drawLines(): 
    alex.speed(0) 
    alex.fillcolor("yellow") 
    alex.begin_fill() 
    alex.penup() 
    alex.setpos(-250, 70) 
    alex.pendown() 
    for i in range(2): 
     alex.forward(500) 
     alex.left(90) 
     alex.forward(30) 
     alex.left(90) 
    alex.end_fill() 

    alex.fillcolor("black") 
    alex.begin_fill() 
    alex.penup() 
    alex.setpos(-250, 40) 
    alex.pendown() 
    for i in range(2): 
     alex.forward(500) 
     alex.left(90) 
     alex.forward(30) 
     alex.left(90) 
    alex.end_fill() 

    alex.pencolor("white") 
    alex.fillcolor("white") 
    alex.begin_fill() 
    alex.penup() 
    alex.setpos(-250, 10) 
    alex.pendown() 
    for i in range(2): 
     alex.forward(500) 
     alex.left(90) 
     alex.forward(30) 
     alex.left(90) 
    alex.end_fill() 

    alex.speed(0) 
    alex.fillcolor("yellow") 
    alex.begin_fill() 
    alex.penup() 
    alex.setpos(-40, -100) 
    alex.pendown() 
    for i in range(2): 
     alex.forward(30) 
     alex.left(90) 
     alex.forward(300) 
     alex.left(90) 
    alex.end_fill() 

    alex.speed(0) 
    alex.fillcolor("black") 
    alex.begin_fill() 
    alex.penup() 
    alex.setpos(-10, -100) 
    alex.pendown() 
    for i in range(2): 
     alex.forward(30) 
     alex.left(90) 
     alex.forward(300) 
     alex.left(90) 
    alex.end_fill() 

    alex.speed(0) 
    alex.pencolor("white") 
    alex.fillcolor("white") 
    alex.begin_fill() 
    alex.penup() 
    alex.setpos(20, -100) 
    alex.pendown() 
    for i in range(2): 
     alex.forward(30) 
     alex.left(90) 
     alex.forward(300) 
     alex.left(90) 
    alex.end_fill() 

drawLines() 

def drawCircle(): 
    alex.speed(0) 
    alex.up() 
    alex.setpos(10, -50) 
    alex.down() 
    alex.fillcolor("red") 
    alex.begin_fill() 
    alex.circle(100) 
    alex.end_fill() 
drawCircle() 

def drawStars(): 
    alex.speed(0) 
    alex.pencolor("green") 
    alex.fillcolor("green") 
    alex.begin_fill() 

    for i in range(5): 
     alex.forward(20) 
     alex.right(144) 

def makeStars(): 
    alex.penup() 
    alex.setpos(25, -10) 
    alex.pendown() 
    for i in range(11): 
     drawStars() 
     alex.left(35) 
     alex.penup() 
     alex.forward(45) 
     alex.pendown() 

makeStars()
