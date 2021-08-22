from turtle import Turtle, heading
ALIGNMENT = 'center'
FONT = ("Arial", 20, "normal")



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
            self.score += 1
            self.clear()
            self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def highest_score(self):
        self.highest_point = 0
        file1 = open('highest_score.txt', 'w')
        if self.score < self.highest_point: 
            file1.write(str(self.score))
            file1.close()
            self.highest_point = self.score
        