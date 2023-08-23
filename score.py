import turtle as t

class Score:
    def __init__(self):
        self.score = t.Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.color('#EEEDED')
        self.score.goto((-350,-300))
        self.score.write(f'Your Score is : 0', align='left',font=('Courier', 16, 'bold'))
        
    def updateScore(self,score):
        self.score.clear()
        self.score.goto((-350,-300))
        self.score.write(f'Your Score is : {score}', align='left',font=('Courier', 16, 'bold'))


    def gameOver(self):
        game = t.Turtle()
        game.hideturtle()
        game.color('#EEEDED')
        game.write('Game Over',align='center', font=('Courier',23,'normal'))