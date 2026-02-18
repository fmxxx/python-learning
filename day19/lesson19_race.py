from turtle import Turtle, Screen

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


def create_turtles(names_colors, start_x, start_y, y_offset):
    turtles = []
    for i, name in enumerate(names_colors):
        t = Turtle()
        t.shape("turtle")
        t.color(names_colors[name])
        t.penup()
        t.teleport(-200, 200 - i * y_offset)
        t.pendown()

        turtles.append(t)


my_screen = Screen()
my_screen.setup(width=500, height=500)

finish_line_x = 200
create_turtles(names_colors, start_x=-200, start_y=200, y_offset=55)

user_bet = my_screen.textinput(title="Make your bet", prompt="Who'll win")
user_bet = user_bet.lower()  # type: ignore

if user_bet not in names_colors:
    my_screen.bye()
    print("This doesn't exist!!!!")

my_screen.exitonclick()
