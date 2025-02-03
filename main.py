from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()
is_game_on = True

while is_game_on:
   screen.update()
   time.sleep(0.1)
   snake.move()
   #collision food
   if snake.all_snake[0].distance(food) < 15:
      food.refresh()
      score.inc_score()
      snake.grow()
   # wall
   if snake.all_snake[0].xcor() > 280 or snake.all_snake[0].xcor() < -280 or snake.all_snake[0].ycor() > 280 or snake.all_snake[0].ycor() < -280:
      is_game_on = False
      score.game_over()

   for segment in snake.all_snake[1:]:
        if snake.all_snake[0].distance(segment) < 15:
            is_game_on = False
            score.game_over()





   

   
    
screen.exitonclick()