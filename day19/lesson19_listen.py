from turtle import Turtle, Screen


def move_forwards():
    a.forward(10)


def move_backwards():
    a.backward(10)


def turn_left():
    a.left(10)


def turn_right():
    a.right(10)


def clear():
    a.clear()


def home():
    a.home()


def penup():
    a.penup()


def pendown():
    a.pendown()


a = Turtle()
my_screen = Screen()
a.speed("fastest")


my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="c", fun=clear)
my_screen.onkey(key="h", fun=home)
my_screen.onkey(key="q", fun=penup)
my_screen.onkey(key="e", fun=pendown)

my_screen.exitonclick()
