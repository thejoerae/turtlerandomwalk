from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)

tim.pensize(10)
tim.speed("fastest")

directions = [0, 90, 180, 270]


def random_move():
    tim.forward(50)
    tim.setheading(random.choice(directions))
    tim.color(random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255))


for _ in range(100):
    random_move()

screen = Screen()
screen.exitonclick()