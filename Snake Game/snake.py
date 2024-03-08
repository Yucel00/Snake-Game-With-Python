from turtle import Turtle
starting_positions=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]



    def create_snake(self):
        for position in starting_positions:
            self.add_segments(position)


    def add_segments(self,position):
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def move(self):
       for seg_num in range(len(self.segments)-1,0,-1):
           new_x=self.segments[seg_num -1].xcor()
           new_y=self.segments[seg_num -1].ycor()
           self.segments[seg_num].goto(new_x,new_y)
       self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segments(self.segments[-1].position())


    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
