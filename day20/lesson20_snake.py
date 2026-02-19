from turtle import Screen, Turtle, Vec2D

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("SNAKE")
screen.no_animation()

snake: list[Turtle] = []


def snake_square() -> Turtle:
    s = Turtle("square")
    s.color("white")
    s.penup()
    return s


def add_tail(snake, latest_move):
    lenght = len(snake)
    s = snake_square()
    print(lenght)

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


def move_snake_n():
    move_snake("n")


def move_snake_s():
    move_snake("s")


def move_snake_e():
    move_snake("e")


def move_snake_w():
    move_snake("w")


for i in range(3):
    add_tail(snake, "e")

for square in snake:
    square.speed(1)

screen.listen()
screen.onkey(key="w", fun=move_snake_n)
screen.onkey(key="s", fun=move_snake_s)
screen.onkey(key="a", fun=move_snake_w)
screen.onkey(key="d", fun=move_snake_e)

screen.exitonclick()
