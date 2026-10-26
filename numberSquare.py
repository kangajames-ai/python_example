# Define a header for the table
print("Number Square")
print("------- --------")

# Use a for loop to iterate from 1 to 10
for num in range(1, 11): # Start at 1, stop before 11 (10)
	# Inside the loop, use the target variable 'num'
	square = num * num # Calculate the square of the current number

	# Print each number and its square in a formatted way
	print(f"{num:4} {square:6}") # Use f-string for formatting