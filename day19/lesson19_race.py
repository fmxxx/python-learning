from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=500, height=500)


turtle_names = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]

finish_line_x = 200
offset = 55

red_t = Turtle()
red_t.shape("turtle")
red_t.color("red")
red_t.penup()
red_t.teleport(-200, 200)

orange_t = Turtle()
orange_t.shape("turtle")
orange_t.color("orange")
orange_t.teleport(-200, 200 - offset)

yellow_t = Turtle()
yellow_t.shape("turtle")
yellow_t.color("yellow")
yellow_t.teleport(-200, 200 - 2 * offset)

green_t = Turtle()
green_t.shape("turtle")
green_t.color("lime")
green_t.teleport(-200, 200 - 3 * offset)

cyan_t = Turtle()
cyan_t.shape("turtle")
cyan_t.color("cyan")
cyan_t.teleport(-200, 200 - 4 * offset)

blue_t = Turtle()
blue_t.shape("turtle")
blue_t.color("blue")
blue_t.teleport(-200, 200 - 5 * offset)

purple_t = Turtle()
purple_t.shape("turtle")
purple_t.color("purple2")
purple_t.teleport(-200, 200 - 6 * offset)

magenta_t = Turtle()
magenta_t.shape("turtle")
magenta_t.color("magenta")
magenta_t.teleport(-200, 200 - 7 * offset)

user_bet = my_screen.textinput(title="Make your bet", prompt="Who'll win")
user_bet = user_bet.lower()  # type: ignore

if user_bet not in turtle_names:
    my_screen.bye()
    print("This doesn't exist!!!!")

my_screen.exitonclick()
