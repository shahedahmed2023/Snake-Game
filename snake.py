from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.all_snake = []
        self.create_snake()
        self.screen = Screen()

    def create_snake(self):
        for postion in STARTING_POSITIONS:
          self.add_snake_piece(postion)
            
    def add_snake_piece(self,distance):
        tim = Turtle('square')
        tim.color('purple')
        tim.penup()
        tim.goto(distance)
        self.all_snake.append(tim)
    
    def grow(self):
        self.add_snake_piece(self.all_snake[-1].position())

    def up(self):
        if self.all_snake[0].heading() != 270:
            self.all_snake[0].setheading(90)
    def down(self ):
        if self.all_snake[0].heading() != 90:
            self.all_snake[0].setheading(270)
    def left(self):
        if self.all_snake[0].heading() != 0:
            self.all_snake[0].setheading(180)
    def right(self):
        if self.all_snake[0].heading() != 180:
            self.all_snake[0].setheading(0)
    
    

        
    def move(self):
        for seg_num in range(len(self.all_snake) -1, 0 , -1):
            new_x = self.all_snake[seg_num - 1].xcor()
            new_y = self.all_snake[seg_num - 1].ycor()
            self.all_snake[seg_num].goto(new_x,new_y)
        self.all_snake[0].forward(20)
        self.screen.listen()
        self.screen.onkey(key='Up' , fun= self.up)
        self.screen.onkey(key='Down' , fun=self.down)
        self.screen.onkey(key='Right' , fun= self.right)
        self.screen.onkey(key='Left' , fun=self.left)
        