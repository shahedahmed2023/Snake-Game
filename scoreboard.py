import turtle
ALIGNMENT = "center"
FONT_FAMILY = "Arial"
SIZE = 24
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0,265)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT,font=(FONT_FAMILY,SIZE,'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Gamer Over",align=ALIGNMENT , font=(FONT_FAMILY,SIZE,'normal'))
       
    def inc_score(self):
        self.score +=1
        self.update_scoreboard()
        

        

