from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
        

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
        
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
            
    if snake.head.xcor() < -300 or snake.head.xcor() > 280 or snake.head.ycor() < -290 or snake.head.ycor() > 300:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            
    
screen.exitonclick()



