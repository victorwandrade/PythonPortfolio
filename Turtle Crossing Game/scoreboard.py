from turtle import Turtle
FONT = ("Courier", 15, "normal")
X_POSITION = -240
Y_POSITION = 270
ALIGNMENT = "center"
GAME_OVER_POSITION = (0,0)


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.up()
        self.hideturtle()
        self.teleport(X_POSITION, Y_POSITION)
        self.write(f"Level: {self.score}", False, align = ALIGNMENT, font = FONT)
    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", False, align = ALIGNMENT, font = FONT)
        return self.score
    
    def game_over(self):
        self.setpos(GAME_OVER_POSITION)
        self.write("Game Over!", False, align = ALIGNMENT, font = FONT)

  
