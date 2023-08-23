import random as r
import turtle as t

SCREENWIDTH = 300
SCREENHEIGHT = 300
class Food:
    def __init__(self):
        x = r.randint(SCREENWIDTH-(SCREENWIDTH*2),SCREENWIDTH)
        y = r.randint(SCREENHEIGHT-(SCREENHEIGHT*2),SCREENHEIGHT)
        food = t.Turtle('circle')
        food.color('#F31559')
        food.penup()
        food.goto(x,y)
        self.food = food

    def makeFood(self):
        x = r.randint(SCREENWIDTH-(SCREENWIDTH*2),SCREENWIDTH)
        y = r.randint(SCREENHEIGHT-(SCREENHEIGHT*2),SCREENHEIGHT)
        self.food.hideturtle()
        food = t.Turtle('circle')
        food.color('#F31559')
        food.penup()
        food.goto(x,y)
        self.food = food
    


