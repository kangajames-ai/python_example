rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for row in range(rows):
        for col in range(cols):
                print("*", end=" ") # Print an asterisk followed by a space for column formatting
        print() # Move to the next line after each row