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


def add_tail(snake: list[Turtle]):
    lenght: int = len(snake)

    s = snake_square()

    if lenght == 0:
        snake.append(s)
    else:
        if snake[0].heading == 0:
            s.teleport(-20 * lenght, 0)
        if snake[0].heading == 90:
            s.teleport(0, -20 * lenght)
        if snake[0].heading == 180:
            s.teleport(20 * lenght, 0)
        if snake[0].heading == 270:
            s.teleport(0, 20 * lenght)
        snake.append(s)


def move_snake(direction: str, heading_map: dict[str, int], grid_size: int):
    assert direction in ["e", "n", "w", "s"]

    # Move tail, position of previous = position of next
    for i in range(len(snake) - 1, 0, -1):
        new_x: float = snake[i - 1].xcor()
        new_y: float = snake[i - 1].ycor()

        snake[i].teleport(x=new_x, y=new_y)
    # Move head
    snake[0].setheading(heading_map[direction])

    if snake[0].heading() == 0.0:
        snake[0].teleport(snake[0].xcor() + grid_size, snake[0].ycor())
    if snake[0].heading() == 90.0:
        snake[0].teleport(snake[0].xcor(), snake[0].ycor() + grid_size)
    if snake[0].heading() == 180.0:
        snake[0].teleport(snake[0].xcor() - grid_size, snake[0].ycor())
    if snake[0].heading() == 270.0:
        snake[0].teleport(snake[0].xcor(), snake[0].ycor() - grid_size)

    return


def set_direction_n():
    if not snake[0].heading() == heading_map["s"]:
        global direction
        direction = "n"


def set_direction_s():
    if not snake[0].heading() == heading_map["n"]:
        global direction
        direction = "s"


def set_direction_e():
    if not snake[0].heading() == heading_map["w"]:
        global direction
        direction = "e"


def set_direction_w():
    if not snake[0].heading() == heading_map["e"]:
        global direction
        direction = "w"


def fail_state():
    return False


def spawn_food() -> Turtle:
    f = Turtle("square")
    f.color("red")
    f.penup()

    return f


def random_food_pos(
    food_min_x: int,
    food_max_x: int,
    food_min_y: int,
    food_max_y: int,
    grid_size: int,
) -> tuple[float, float]:
    # TODO calculate x and y so it doesn't intersect with border
    # regardless of sign (- , +) of min and max values
    food_x: float = float(random.randint(food_min_x + 1, food_max_x - 1) * grid_size)
    food_y: float = float(random.randint(food_min_y + 1, food_max_y - 1) * grid_size)

    return (food_x, food_y)


# PROGRAM START
screen = Screen()
screen.setup(width=850, height=850)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(False)
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

screen.listen()
screen.onkey(key="w", fun=set_direction_n)
screen.onkey(key="s", fun=set_direction_s)
screen.onkey(key="a", fun=set_direction_w)
screen.onkey(key="d", fun=set_direction_e)

snake: list[Turtle] = []
for i in range(3):
    add_tail(snake)

food: Turtle = spawn_food()
new_pos: tuple[float, float] = random_food_pos(-20, 20, -20, 20, grid_size)
food.teleport(x=new_pos[0], y=new_pos[1])

direction: str = "e"
is_game_on: bool = True

while is_game_on:
    # Check Border collision
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

    # Check if food is eaten
    if snake[0].xcor() == food.xcor() and snake[0].ycor() == food.ycor():
        add_tail(snake)
        # TODO change it to calculate based on border size and starting pos
        # and divide by 20 (pixel size)
        new_pos = random_food_pos(-20, 20, -20, 20, grid_size)
        food.teleport(x=new_pos[0], y=new_pos[1])

    move_snake(direction, heading_map, grid_size)
    screen.update()
    time.sleep(game_clock_s)


screen.exitonclick()
