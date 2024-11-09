import turtle

def draw_petal(t):
    t.circle(100, 60)  # Draw the first arc of the petal
    t.left(120)        # Turn left
    t.circle(100, 60)  # Draw the second arc of the petal
    t.left(120)        # Turn left to the original direction

def draw_flower(t, petals):
    for _ in range(petals):
        draw_petal(t)
        t.left(360 / petals)  # Position for the next petal

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("red")
    t.speed(10)

    draw_flower(t, 8)  # You can change the number of petals here

    t.hideturtle()
    turtle.done()

if __name__ == "_main_":
    main()