from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        # Inheritance from Turtle class
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle() # Hide the turtle
        self.penup() # Don't draw lines
        self.goto(0, 270)
        self.increase_score()
        
    # Increase the score by 1
    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1
    
    # Game over message
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)