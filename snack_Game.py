from distutils.dep_util import newer_pairwise
from turtle import Turtle, xcor 
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DICTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class snake:

    def __init_(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segmant(position)
    
    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)

    def extend(self):
        self.add_segment(self.segment[-1].position()) 


    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg_num-1],xcor()
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DICTANCE)
    
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heqading()!=RIGHT:
            self.head.setheading(LEFT)
    
    