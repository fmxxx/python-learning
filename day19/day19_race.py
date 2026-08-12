from turtle import Turtle, Screen
import random


names_colors = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "lime",
    "cyan": "cyan",
    "blue": "blue",
    "purple": "purple2",
    "magenta": "magenta",
}


def create_turtles(names_colors, start_x, start_y, y_offset) -> list[Turtle]:
    turtles = []
    for i, name in enumerate(names_colors):
        t = Turtle()
        t.shape("turtle")
        t.color(names_colors[name])
        t.penup()
        t.teleport(start_x, start_y - i * y_offset)
        t.pendown()

        turtles.append(t)
    return turtles


def race(turtles: list[Turtle], finish_line_x: int, step_min: int, step_max: int):
    assert step_max * step_min > 0, "Steps must be in the same direciton and positive"
    assert (
        step_min * finish_line_x > 0
    ), "Finish line must be in same direction of steps"

    is_finished = False
    winner = None

    for turtle in turtles:
        turtle.setheading(0)

    while not is_finished:
        for turtle in turtles:
            turtle.forward(random.randint(step_min, step_max))
            pos = turtle.position()
            if pos[0] >= finish_line_x:
                is_finished = True
                winner = turtle
                break

    return winner


my_screen = Screen()
my_screen.setup(width=500, height=500)

finish_line_x = 200
turtles = create_turtles(names_colors, start_x=-200, start_y=200, y_offset=55)

user_bet = my_screen.textinput(title="Make your bet", prompt="Who'll win")
user_bet = user_bet.lower()  # type: ignore

if user_bet not in names_colors:
    my_screen.bye()
    print("This doesn't exist!!!!")

winner = race(turtles, finish_line_x, 5, 10)
assert winner is not None, "Race should always have a winner"
winner_name = winner.color()[0]

print(f"Winner was: {winner_name.upper()}!")

if winner_name == names_colors[user_bet]:
    print("YOU WIN!")
else:
    print("You lost :(")

my_screen.exitonclick()
