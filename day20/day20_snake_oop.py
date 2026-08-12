from turtle import Screen, Turtle, Vec2D
import random, time

# TODO: Initialize the atributes by passing them in the init method, instead
# of setting them after using the init method.
class Snake_Squares(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()


    def set_random_pos(self,
        food_min_x: int,
        food_max_x: int,
        food_min_y: int,
        food_max_y: int,
        grid_size: int,
    ) -> None:
        # TODO calculate x and y so it doesn't intersect with border
        # regardless of sign (- , +) of min and max values
        food_x: float = float(random.randint(food_min_x + 1, food_max_x - 1) * grid_size)
        food_y: float = float(random.randint(food_min_y + 1, food_max_y - 1) * grid_size)

        self.teleport(food_x, food_y)


class Snake(Turtle):
    default_direction = "e"

    def __init__(self) -> None:
        super().__init__()

        self.direction = self.default_direction
        self.body: list[Snake_Squares] = []
        for i in range(3):
            self.grow_tail()

    def grow_tail(self):
        lenght: int = len(self.body)

        s = Snake_Squares()

        if lenght == 0:
            self.body.append(s)
        else:
            if self.body[0].heading == 0:
                s.teleport(-20 * lenght, 0)
            if self.body[0].heading == 90:
                s.teleport(0, -20 * lenght)
            if self.body[0].heading == 180:
                s.teleport(20 * lenght, 0)
            if self.body[0].heading == 270:
                s.teleport(0, 20 * lenght)
            self.body.append(s)

    def move(
        self,
        heading_map,
        grid_size):
        assert self.direction in ["e", "n", "w", "s"]

        # Move tail, position of previous = position of next
        for i in range(len(self.body) - 1, 0, -1):
            new_x: float = self.body[i - 1].xcor()
            new_y: float = self.body[i - 1].ycor()

            self.body[i].teleport(x=new_x, y=new_y)
        # Move head
        self.body[0].setheading(heading_map[self.direction])

        if self.body[0].heading() == 0.0:
            self.body[0].teleport(self.body[0].xcor() + grid_size, self.body[0].ycor())
        if self.body[0].heading() == 90.0:
            self.body[0].teleport(self.body[0].xcor(), self.body[0].ycor() + grid_size)
        if self.body[0].heading() == 180.0:
            self.body[0].teleport(self.body[0].xcor() - grid_size, self.body[0].ycor())
        if self.body[0].heading() == 270.0:
            self.body[0].teleport(self.body[0].xcor(), self.body[0].ycor() - grid_size)

        return

    def has_touched_border(self, inner_abs_border_x, inner_abs_border_y):
        if (abs(player_snake.body[0].xcor()) == inner_abs_border_x
        or abs(player_snake.body[0].ycor()) == inner_abs_border_y):
            return True
        else:
            return False

    def has_touched_food(self, food):

        if player_snake.body[0].xcor() == food.xcor() and player_snake.body[0].ycor() == food.ycor():
            player_snake.grow_tail()
            return True
        else:
            return False

    def set_dir_n(self):
        if not self.body[0].heading() == heading_map["s"]:
            self.direction = "n"

    def set_dir_s(self):
        if not self.body[0].heading() == heading_map["n"]:
            self.direction = "s"

    def set_dir_e(self):
        if not self.body[0].heading() == heading_map["w"]:
            self.direction = "e"

    def set_dir_w(self):
        if not self.body[0].heading() == heading_map["e"]:
            self.direction = "w"


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


def fail_state():
    return False


# PROGRAM START
screen = Screen()
screen.setup(width=850, height=850)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(False)

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
player_snake = Snake()

screen.listen()
screen.onkey(key="w", fun=player_snake.set_dir_n)
screen.onkey(key="s", fun=player_snake.set_dir_s)
screen.onkey(key="a", fun=player_snake.set_dir_w)
screen.onkey(key="d", fun=player_snake.set_dir_e)


food = Food()
food.set_random_pos(-20, 20, -20, 20, grid_size)

is_game_on: bool = True

while is_game_on:
    player_snake.move(heading_map, grid_size)
    screen.update()

    # Check Border collision
    if player_snake.has_touched_border(inner_abs_border_x, inner_abs_border_y):
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

    # Check if food is eaten
    if player_snake.has_touched_food(food):
        # TODO change it to calculate based on border size and starting pos
        # and divide by 20 (pixel size)
        food.set_random_pos(-20, 20, -20, 20, grid_size)

    time.sleep(game_clock_s)

screen.exitonclick()
