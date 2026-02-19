from turtle import Screen, Turtle, Vec2D
import random, time


def draw_border(width: int, height: int, start_x: int, start_y: int):
    b = Turtle(visible=False)
    b.speed("fastest")
    b.color("gray")
    b.teleport(start_x, start_y)
    b.pensize(20)

    b.forward(width)
    b.right(90)
    b.forward(height)
    b.right(90)
    b.forward(width)
    b.right(90)
    b.forward(height)


def snake_square() -> Turtle:
    s = Turtle("square")
    s.color("white")
    s.penup()
    return s


def add_tail(snake, latest_move):
    lenght = len(snake)

    s = snake_square()

    if lenght == 0:
        snake.append(s)
    else:
        if latest_move == "e":
            s.teleport(-20 * lenght, 0)
        if latest_move == "n":
            s.teleport(0, -20 * lenght)
        if latest_move == "w":
            s.teleport(20 * lenght, 0)
        if latest_move == "s":
            s.teleport(0, 20 * lenght)
        snake.append(s)


def move_snake(direction):
    assert direction in ["n", "s", "e", "w"]

    next_pos: Vec2D = snake[0].pos()

    if direction == "e":
        snake[0].teleport(x=next_pos[0] + 20, y=next_pos[1])
    if direction == "n":
        snake[0].teleport(x=next_pos[0], y=next_pos[1] + 20)
    if direction == "w":
        snake[0].teleport(x=next_pos[0] - 20, y=next_pos[1])
    if direction == "s":
        snake[0].teleport(x=next_pos[0], y=next_pos[1] - 20)

    for i, square in enumerate(snake[:-1]):
        i = i + 1
        next_next_pos: Vec2D = snake[i].pos()
        snake[i].teleport(x=next_pos[0], y=next_pos[1])
        next_pos = next_next_pos

    screen.update()


def set_direction_n():
    global direction
    direction = "n"


def set_direction_s():
    global direction
    direction = "s"


def set_direction_e():
    global direction
    direction = "e"


def set_direction_w():
    global direction
    direction = "w"


# PROGRAM START
screen = Screen()
screen.setup(width=850, height=850)
screen.bgcolor("black")
screen.title("SNAKE")
screen.no_animation()
screen.tracer(0)

draw_border(780, 780, -400, 400)

snake: list[Turtle] = []

for i in range(3):
    add_tail(snake, "e")

screen.update()

screen.listen()
screen.onkey(key="w", fun=set_direction_n)
screen.onkey(key="s", fun=set_direction_s)
screen.onkey(key="a", fun=set_direction_w)
screen.onkey(key="d", fun=set_direction_e)


is_game_on = True
direction: str = "e"

while is_game_on:
    move_snake(direction)
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
