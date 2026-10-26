'''import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

def main():
    screen = turtle.Screen()
    screen.title("Turtle Graphics Patterns")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(1)  # Slow speed for visibility

    # Draw a square
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    draw_square(t, 100)

    # Draw a triangle
    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_triangle(t, 100)

    # Draw a star
    t.penup()
    t.goto(200, 0)
    t.pendown()
    draw_star(t, 100)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()'''

import turtle
print(dir(turtle))  # Should show 'Screen' in the list