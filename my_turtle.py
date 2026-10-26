import turtle

def setup_screen():
    """Initialize the turtle screen with basic settings"""
    screen = turtle.Screen()
    screen.title("Turtle Graphics Patterns - PROG103 Final Project")
    screen.bgcolor("lightgray")
    return screen

def draw_square(size, color):
    """Draw a square with given size and color"""
    turtle.penup()
    turtle.goto(-size//2, size//2)
    turtle.pendown()
    turtle.color(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

def draw_triangle(size, color):
    """Draw an equilateral triangle with given size and color"""
    turtle.penup()
    turtle.goto(0, size)
    turtle.pendown()
    turtle.color(color)
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

def draw_star(size, color):
    """Draw a 5-pointed star with given size and color"""
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color(color)
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_spiral(size, turns, color):
    """Draw a spiral with given parameters"""
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color(color)
    for i in range(turns):
        turtle.forward(i * 5)
        turtle.right(90)

def draw_circle(size, color):
    """Draw a circle with given radius and color"""
    turtle.penup()
    turtle.goto(0, -size)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(size)

def reset_turtle():
    """Reset turtle position and clear drawing"""
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def main():
    """Main program with user menu"""
    screen = setup_screen()
    turtle.speed(1)  # Set drawing speed (1=slowest, 10=fastest)
    
    while True:
        print("\n==== Turtle Graphics Menu ====")
        print("1. Draw Square")
        print("2. Draw Triangle")
        print("3. Draw Star")
        print("4. Draw Spiral")
        print("5. Draw Circle")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            size = int(input("Enter square size (50-300): "))
            color = input("Enter color (e.g., red, blue, green): ")
            reset_turtle()
            draw_square(size, color)
            
        elif choice == "2":
            size = int(input("Enter triangle size (50-300): "))
            color = input("Enter color: ")
            reset_turtle()
            draw_triangle(size, color)
            
        elif choice == "3":
            size = int(input("Enter star size (50-300): "))
            color = input("Enter color: ")
            reset_turtle()
            draw_star(size, color)
            
        elif choice == "4":
            size = int(input("Enter spiral size (10-100): "))
            turns = int(input("Enter number of turns (5-20): "))
            color = input("Enter color: ")
            reset_turtle()
            draw_spiral(size, turns, color)
            
        elif choice == "5":
            size = int(input("Enter circle radius (50-200): "))
            color = input("Enter color: ")
            reset_turtle()
            draw_circle(size, color)
            
        elif choice == "6":
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1-6.")
    
    turtle.done()

if __name__ == "__main__":
    main()