from turtle import *

coordinate = 0

degree = 90

step = 100

def coordinate_system(): # 建立坐标系函数
    
    speed(0)
    
    dot(10, "red")
    
    pencolor("LightGrey") 
      
    row_y = 300
    
    for i in range(int(600 / 20 - 1)):
        
        row_y -= 20
        
        up()
        
        goto(-300, row_y)
        
        down()
        
        fd(600)
 
    right(90)
        
    column_x = -300
    
    for i in range(int(600 / 20 - 1)):
        
        column_x += 20
        
        up()
        
        goto(column_x, 300)
        
        down()
        
        fd(600)
        
    up()
    
    home() # 回到初始位置(坐标和方向)
    
    down()

def ready():

    speed(1)

    pensize(10)

    bgcolor("black")

    setup(width=1440, height=900, startx = coordinate, starty = coordinate)
    


def draw_a_square():
    
    colors = ["blue", "purple", "pink", "white"]
    
    fillcolor("#DC143C")

    begin_fill()

    for color in colors:

        pencolor(color)

        fd(step)

        right(degree)

    end_fill()

def done():
    
    coordinate_system() 

    ready()

    draw_a_square()
    

done()
