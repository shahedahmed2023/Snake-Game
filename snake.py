from turtle import Turtle, Screen

# Initial positions for the snake's starting body parts
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.all_segments = []  # List to store all snake segments
        self.create_snake()  # Create the initial snake
        self.screen = Screen()  # Reference to the screen for listening to key presses

    def create_snake(self):
        """Creates the snake with three initial segments."""
        for position in STARTING_POSITIONS:
            self.add_snake_piece(position)

    def reset(self):
        """Resets the snake by removing all segments and creating a new one."""
        for seg in self.all_segments:
            seg.goto(1000, 1000)  # Move segments off-screen before clearing
        self.all_segments.clear()
        self.create_snake()  # Recreate the snake

    def add_snake_piece(self, position):
        """Adds a new segment to the snake at the given position."""
        segment = Turtle('square')
        segment.color('purple')
        segment.penup()
        segment.goto(position)
        self.all_segments.append(segment)

    def grow(self):
        """Grows the snake by adding a new segment at the last segment's position."""
        self.add_snake_piece(self.all_segments[-1].position())

    def up(self):
        """Changes direction to up unless currently moving down."""
        if self.all_segments[0].heading() != 270:
            self.all_segments[0].setheading(90)

    def down(self):
        """Changes direction to down unless currently moving up."""
        if self.all_segments[0].heading() != 90:
            self.all_segments[0].setheading(270)

    def left(self):
        """Changes direction to left unless currently moving right."""
        if self.all_segments[0].heading() != 0:
            self.all_segments[0].setheading(180)

    def right(self):
        """Changes direction to right unless currently moving left."""
        if self.all_segments[0].heading() != 180:
            self.all_segments[0].setheading(0)

    def move(self):
        """Moves the snake forward by shifting each segment to the position of the previous one."""
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)
        self.all_segments[0].forward(20)  # Move the head forward

        # Listen for key presses in the main game loop
        self.screen.listen()
        self.screen.onkey(self.up, 'Up')
        self.screen.onkey(self.down, 'Down')
        self.screen.onkey(self.right, 'Right')
        self.screen.onkey(self.left, 'Left')
