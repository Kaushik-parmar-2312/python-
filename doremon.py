from turtle import *

setup(500,500)
speed(10)
bgcolor("black")
shape("turtle")
colormode(255)

def drawRoumd(size,filled):
    pendown()
    if filled==True:
        begin_fill()
    setheading (180)
    circle(size,360)
    if filled==True:
        end_fill()
def drawRect(length,width,filled):
    setheading(0)
    pendown()
    if filled==True:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if filled==True:
        end_fill()

def head():
    color("blue","blue") 
    penup()
    goto(0,100)
    drawRoumd(75,True)
    #
    color("white","white")
    penup()
    goto(0,72)
    drawRoumd(60,True)

def eyes():
    #left Eye socket
    color("black","white")
    penup()
    goto(-15,80)
    drawRoumd(17,True)      
    
    #Right Eye socket
    color("black","white")
    penup()
    goto(19,80)
    drawRoumd(17,True) 
    
    #
    color("black","black")
    penup()
    goto(-8,70)
    drawRoumd(6,True)
    color("white","white")
    penup()
    goto(-8,66)
    drawRoumd(2,True)
    
    #Right Eyeball
    color("black","black")
    penup()
    goto(12,70)
    drawRoumd(6,True)
    color("white","white")
    penup()
    goto(12,66)
    drawRoumd(2,True)

def nose():
    color("red","red")
    penup()
    goto(0,40)
    drawRoumd(7,True)
    
def mouth():
    color("black","black")
    penup()
    goto(-30,-20)
    pendown()
    setheading(-27)
    circle(70,55)
    #
    penup()
    goto(0,26)
    pendown()
    goto(0,-25)

def whiskers():
    color("black","black")
    #The beard in the middle on the left
    penup()
    goto(- 10,5)
    pendown()
    goto(-40,5)
    #The beard in the middle on the right
    penup()
    goto(10,5)
    pendown()
    goto(40,5)
    #left uppper beard
    penup()
    goto(-10,15)
    pendown()
    goto(-40,20)
    #The bread on the upper right
    penup()
    goto(10,15)
    pendown()
    goto(40,20)
    #leftbread
    penup()
    goto(-10,-5)
    pendown()
    goto(-40,-10)
    #bread on the lower right
    penup()
    goto(10,-5)
    pendown()
    goto(40,-10)

def body():
#blue body
    color("blue","blue")
    penup()
    goto(-50,-40)
    drawRect(100,80,True)
#white belly
    color("white","white")
    penup()
    goto(0,-30)
    drawRoumd(40,True)
#Red Ribbon
    color("Red","Red")
    penup()
    goto(-60,-35)
    drawRect(120,10,True)
#white legs
    color("white","white")
    penup()
    goto(15,-127)
    pendown()
    setheading(90)
    begin_fill()
    circle(14,180)
    end_fill()

def feet():
    #left foot
    color("black","white")
    penup()
    goto(-30,-110)
    drawRoumd(20,True)
    #right left
    color("black","white")
    penup()
    goto(30,-110)
    drawRoumd(20,True)

def arms():
    #left arm
    color("blue","blue")
    penup()
    begin_fill()
    goto(-51,-50)
    pendown()
    goto(-51,-75)
    left(70)
    goto(-76,-85)
    left(70)
    goto(-86,-70)
    left(70)
    goto(-51,-50)
    end_fill()
    #right arm
    color("blue","blue")
    penup()
    begin_fill()
    goto(49,-50)
    pendown()
    goto(49,-75)
    left(70)
    goto(74,-85)
    left(70)
    goto(84,-70)
    left(70)
    goto(49,-50)
    end_fill()

def hands():
    #lefthand
    color("black","white")
    penup()
    goto(-90,-71)
    drawRoumd(15,True)
    #right hand
    color("black","white")
    penup()
    goto(90,-71)
    drawRoumd(15,True)

def bell():
    #yellow solid circle indicates coper bell
    color("yellow","yellow")
    penup()
    goto(0,-41)
    drawRoumd(8,True)
    #black Rectangle indicates pattern
    color("black","black")
    penup()
    goto(-10,-47)
    drawRect(20,4,False)
    #the black solid cirle indicates the impacted metal pill
    color("black","black")
    penup()
    goto(0,53)
    drawRoumd(2,True)

def package():
    #semicircle
    color("black","black")
    penup()
    goto(-25,-70)
    pendown()
    setheading(-90)
    circle(25,180)
    goto(-25,-70)
    hideturtle()
    
head()
eyes()
nose()
mouth()
whiskers()

body()
feet()
arms()
hands()
bell()
package()
