import turtle as t
from food import Food

SCREENHEIGHT = 300
SCREENWIDTH= 400

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.positions = [(20,0),(0,0),(-20,0)]
        self.boxes = []
    
    def createSnake(self):
        for i in range(3):
            newBox = t.Turtle('square')
            newBox.color('#64CCC5')
            newBox.penup()
            newBox.goto(self.positions[i])
            self.boxes.append(newBox)
        self.head = self.boxes[0]
        
    def move(self):
        for i in range(len(self.boxes)-1,0,-1):
            x = self.boxes[i-1].xcor()
            y = self.boxes[i-1].ycor()
            self.boxes[i].goto((x,y))
        self.head.forward(20)
        self.checkScreen()
        
        
    def moveUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.checkScreen()
        
    def moveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.checkScreen()

    def moveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.checkScreen()

    def moveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.checkScreen()

    def eatFood(self):
        newBox = t.Turtle('square')
        newBox.color('#64CCC5')
        newBox.penup()
        newBox.goto(self.boxes[len(self.boxes)-1].xcor(),self.boxes[len(self.boxes)-1].ycor())
        self.boxes.append(newBox)

    def checkScreen(self):
        if(self.head.xcor() >= SCREENWIDTH):
            print(self.head.xcor(),self.head.ycor())
            self.head.goto(-SCREENWIDTH,self.head.ycor())
        elif(self.head.xcor() <= -SCREENWIDTH):
            print(self.head.xcor(),self.head.ycor())
            self.head.goto(SCREENWIDTH,self.head.ycor())
        
        if(self.head.ycor() >= SCREENHEIGHT):
            print(self.head.xcor(),self.head.ycor())
            self.head.goto(self.head.xcor(),-SCREENHEIGHT)
        elif(self.head.ycor() <= -SCREENHEIGHT):
            print(self.head.xcor(),self.head.ycor())
            self.head.goto(self.head.xcor(),SCREENHEIGHT)
