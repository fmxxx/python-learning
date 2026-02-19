from turtle import Screen, Turtle, Vec2D
import random, time


def draw_border(
    width: int, height: int, start_x: int, start_y: int, color: str, grid_size: int
):
    b = Turtle(visible=False)
    b.speed("fastest")
    b.color(color)
    b.teleport(start_x, start_y)
    b.pensize(grid_size)

    b.forward(width)
    b.right(90)
    b.forward(height)
    b.right(90)
    b.forward(width)
    b.right(90)
    b.forward(height)

    return b


def snake_square() -> Turtle:
    s = Turtle("square")
    s.color("white")
    s.penup()
    return s


def add_tail(snake: list[Turtle], latest_move: str):
    lenght: int = len(snake)

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


def move_snake(direction: str, heading_map: dict[str, int], grid_size: int):
    assert direction in ["e", "n", "w", "s"]

    # Prevent turning 180deg
    if snake[0].heading() == heading_map["e"] and direction == "w":
        direction = "e"
    if snake[0].heading() == heading_map["n"] and direction == "s":
        direction = "n"
    if snake[0].heading() == heading_map["w"] and direction == "e":
        direction = "w"
    if snake[0].heading() == heading_map["s"] and direction == "n":
        direction = "s"

    # Move head
    next_pos: Vec2D = snake[0].pos()

    if direction == "e":
        snake[0].teleport(x=next_pos[0] + grid_size, y=next_pos[1])
    if direction == "n":
        snake[0].teleport(x=next_pos[0], y=next_pos[1] + grid_size)
    if direction == "w":
        snake[0].teleport(x=next_pos[0] - grid_size, y=next_pos[1])
    if direction == "s":
        snake[0].teleport(x=next_pos[0], y=next_pos[1] - grid_size)

    snake[0].setheading(heading_map[direction])

    # Update Tail
    for i, square in enumerate(snake[:-1]):
        i = i + 1
        next_next_pos: Vec2D = snake[i].pos()
        snake[i].teleport(x=next_pos[0], y=next_pos[1])
        next_pos = next_next_pos

    screen.update()
    return


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


def fail_state():
    return False


def spawn_food(
    food_min_x: int, food_max_x: int, food_min_y: int, food_max_y: int, grid_size: int
):
    # TODO calculate x and y so it doesn't intersect with border
    # regardless of sign (- , +) of min and max values
    food_x: int = random.randint(food_min_x + 1, food_max_x - 1) * grid_size
    food_y: int = random.randint(food_min_y + 1, food_max_y - 1) * grid_size

    f = Turtle("square")
    f.color("red")
    f.penup()
    f.teleport(x=food_x, y=food_y)


# PROGRAM START
screen = Screen()
screen.setup(width=850, height=850)
screen.bgcolor("black")
screen.title("SNAKE")
screen.no_animation()
screen.tracer(0)

grid_size: int = 20
game_clock_s: float = 0.1

border_width: int = 800
border_height: int = 800
border_start_x: int = -400
border_start_y: int = 400
inner_abs_border_x: int = abs(border_start_x)
inner_abs_border_y: int = abs(border_start_y)
border = draw_border(
    border_width, border_height, border_start_x, border_start_y, "gray", grid_size
)

heading_map: dict[str, int] = {"e": 0, "n": 90, "w": 180, "s": 270}

snake: list[Turtle] = []

for i in range(3):
    add_tail(snake, "e")

screen.update()

screen.listen()
screen.onkey(key="w", fun=set_direction_n)
screen.onkey(key="s", fun=set_direction_s)
screen.onkey(key="a", fun=set_direction_w)
screen.onkey(key="d", fun=set_direction_e)


is_game_on: bool = True
is_food_collected: bool = True
direction: str = "e"

while is_game_on:
    if is_food_collected:
        # TODO change it to calculate based on border size and starting pos
        # and divide by 20 (pixel size)
        spawn_food(-20, 20, -20, 20, grid_size)
        is_food_collected = False

    move_snake(direction, heading_map, grid_size)
    time.sleep(game_clock_s)
    screen.update()
    if (
        abs(snake[0].xcor()) == inner_abs_border_x
        or abs(snake[0].ycor()) == inner_abs_border_y
    ):
        is_game_on = fail_state()
        border = draw_border(
            border_width,
            border_height,
            border_start_x,
            border_start_y,
            "red",
            grid_size,
        )
        screen.update()

screen.exitonclick()
