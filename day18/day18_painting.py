import colorgram, turtle, random


def dot_grid(turtle, lines, dots_per_line, dot_size, spacing, rgb_colors):
    t.penup()
    for i in range(lines):
        for j in range(dots_per_line):
            turtle.dot(dot_size, random.choice(rgb_colors))
            turtle.forward(spacing)
        turtle.right(90)
        turtle.forward(spacing)
        turtle.right(90)
        turtle.forward(spacing * dots_per_line)
        turtle.right(180)


"""
print("Gimme an image")
img_path = input(">")
print("How many colors?")
color_amt = int(input(">"))
"""

img_path = "C:\\Users\\ffw\\Downloads\\Bhishn_1200x1200-121110327.jpg"
color_amt = 80

extracted_colors = colorgram.extract(img_path, color_amt)

rgb_colors = []
for i in extracted_colors:
    rgb_colors.append(i.rgb)

turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")

t.teleport(-300, 300)
dot_grid(t, 20, 20, 10, 15, rgb_colors)
t.hideturtle()

turtle.exitonclick()
