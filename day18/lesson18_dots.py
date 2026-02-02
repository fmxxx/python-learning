from turtle import Turtle, Screen
import tkinter
import random

timmy = Turtle()
timmy.shape("circle")


def square(
    turtle_obj: Turtle, side_len: int, turns: int = 4, direction: str = "right"
) -> None:
    if direction == "left":
        for _ in range(turns):
            turtle_obj.left(90)
            turtle_obj.forward(side_len)
    elif direction == "right":
        for _ in range(turns):
            turtle_obj.right(90)
            turtle_obj.forward(side_len)
    else:
        raise ValueError("direction must be 'l' or 'r'")


def dashed_line(
    turtle_obj: Turtle, line_size: int, gap_size: int, repeats: int
) -> None:
    for i in range(0, repeats):
        turtle_obj.forward(line_size)
        turtle_obj.penup()
        turtle_obj.forward(gap_size)
        turtle_obj.pendown()


dashed_line(timmy, 10, 10, 10)

"""
square(timmy, 100, 4, "right")
timmy.forward(100)
square(timmy, 100, 3, "left")
square(timmy, 100, 3, "right")
timmy.right(90)
timmy.forward(100)
timmy.forward(100)
square(timmy, 100, 3, "left")
"""

screen = Screen()
screen.exitonclick()
