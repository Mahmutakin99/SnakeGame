from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        # Inheritance from Turtle class
        super().__init__()
        self.shape("circle") # Change the shape of the turtle
        self.penup() # Don't draw lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest") # Speed of the turtle
        self.refresh()
    
    # Refresh the food position
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 265)
        self.goto(random_x, random_y)