from snake import Snake 
from food import Food 
from score import Score 
import turtle as t
import time


GAME = True
SPEED = 0.1
yourScore= 0

screen = t.Screen()
screen.bgcolor('#001C30')
screen.setup(width=400,height=400,startx=100,starty=100)
screen.title('Snake Game - Let\'s Hit the Memories')
screen.tracer(0)

score = Score()
f = Food()
s = Snake()
s.createSnake()


screen.listen()
screen.onkey(s.moveUp,'Up')
screen.onkey(s.moveDown,'Down')
screen.onkey(s.moveLeft,'Left')
screen.onkey(s.moveRight,'Right')


while GAME:
    screen.update()
    time.sleep(SPEED)
    s.move()
    if s.head.distance(f.food) < 20:
        s.eatFood()
        yourScore +=1
        score.updateScore(yourScore)
        f.makeFood()

    for box in s.boxes[1:]:
        if box.distance(s.head) < 15:
            s.head.color('black')
            score.gameOver()
            GAME = False 





screen.exitonclick()
