print("Mai Xuân Huy")
print("MSSV:235752021610062")
import turtle
import random


colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]


painter = turtle.Turtle()
painter.pensize(3) 

for i in range(12):
    color = random.choice(colors)  
    painter.pencolor(color)  
    painter.circle(100) 
    painter.right(30)  
    painter.left(60)  
    painter.setposition(0, 0)  


turtle.done()
