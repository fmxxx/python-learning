import random, turtle
from turtle import Turtle, Screen
from colorsys import hsv_to_rgb
from lesson18_trinket_colors import trinket_colors


turtle.colormode(255)
timmy = Turtle()
timmy.shape("circle")
directions = [0, 90, 180, 270]


def random_rgb():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def random_hsv() -> tuple[float, float, float]:
    h = random.random()
    s = 1
    v = 1
    return (h, s, v)


def square(
    turtle_obj: Turtle, side_len: int, turns: int = 4, direction: str = "r"
) -> None:
    if direction == "l":
        for _ in range(turns):
            turtle_obj.left(90)
            turtle_obj.forward(side_len)
    elif direction == "r":
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


def regular_polygon(turtle_obj: Turtle, side_len: int, sides: int):
    turn_angle = 360 / sides
    for _ in range(sides):
        turtle_obj.left(turn_angle)
        turtle_obj.forward(side_len)


def random_walk(turtle_obj: Turtle, side_len: int, walks: int):
    for i in range(walks + 1):
        turtle_obj.color(random_rgb())
        turtle_obj.right(random.choice(directions))
        turtle_obj.forward(side_len)


def spirograph(turtle_obj: Turtle, radius: int, turns: int):
    for _ in range(turns):
        turtle_obj.circle(radius)
        turtle_obj.left(360 / turns)


timmy.speed("fastest")

timmy.pensize(2)


for i in range(200):
    a = random_hsv()
    a = hsv_to_rgb(*a)
    b = (int(a[0] * 255), int(a[1] * 255), int(a[2] * 255))
    timmy.pencolor(b)
    spirograph(timmy, 150, i)
    timmy.clear()

"""
dashed_line(timmy, 10, 10, 10)
for i in range(3, 10 + 1):
    regular_polygon(timmy, 100, i)

timmy.pensize(10)
random_walk(timmy, 20, 800)

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
