from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)  # Turns off automatic screen updates for smooth movement

# Create game objects
snake = Snake()
food = Food()
score = Scoreboard()
is_game_on = True  # Game loop control variable

while is_game_on:
    screen.update()  # Refresh the screen
    time.sleep(0.1)  # Pause to control game speed
    snake.move()  # Move the snake forward

    # Detect collision with food
    if snake.all_segments[0].distance(food) < 15:
        food.refresh()  # Move food to a new random location
        score.inc_score()  # Increase the score
        snake.grow()  # Extend the snake's body

    # Detect collision with walls
    if snake.all_segments[0].xcor() > 280 or snake.all_segments[0].xcor() < -280 or \
       snake.all_segments[0].ycor() > 280 or snake.all_segments[0].ycor() < -280:
        score.reset()  # Reset the score
        snake.reset()  # Reset the snake to its starting position

    # Detect collision with its own body
    for segment in snake.all_segments[1:]:
        if snake.all_segments[0].distance(segment) < 15:
            score.reset()  # Reset the score
            snake.reset()  # Reset the snake

# Close the game window when clicked
screen.exitonclick()
