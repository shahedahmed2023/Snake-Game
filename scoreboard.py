import turtle

# Constants for text alignment and font
ALIGNMENT = "center"
FONT_FAMILY = "Arial"
SIZE = 24

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        # Read high score from file
        with open("Data.txt", mode='r') as data:
            self.high_score = int(data.read())

        self.color('white')
        self.penup()
        self.goto(0, 265)  # Position the scoreboard at the top
        self.update_scoreboard()
        self.hideturtle()  # Hide the turtle cursor

    def update_scoreboard(self):
        """Updates the scoreboard display."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", 
                   align=ALIGNMENT, font=(FONT_FAMILY, SIZE, 'normal'))

    def reset(self):
        """Resets the current score and updates the high score if needed."""
        if self.score > self.high_score:
            self.high_score = self.score  # Update high score
        
        # Save the high score to the file
        with open("Data.txt", mode='w') as data:
            data.write(str(self.high_score))  # Fix: Store high score, not current score

        self.score = 0  # Reset the current score
        self.update_scoreboard()

    # def game_over(self):
    #     """Displays a game over message."""
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=(FONT_FAMILY, SIZE, 'normal'))

    def inc_score(self):
        """Increases the score and updates the scoreboard."""
        self.score += 1
        self.update_scoreboard()
