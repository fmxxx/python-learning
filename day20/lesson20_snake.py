from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("SNAKE")

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


for i in range(3):
    add_tail(snake, "e")


screen.exitonclick()
