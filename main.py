import turtle
from turtle import Turtle, Screen
import random

colours = ["red", "blue", "orange", "black", "green"]
directions = [0, 90, 180, 270]


tim = Turtle()
# tim.shape("turtle")
turtle.colormode(255)
tim.speed("fastest")
tim.pensize(5)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

for _ in range(200):
    # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))

# screen = Screen()
# screen.exitonclick()
