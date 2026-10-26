even_count = 0
odd_count = 0

num_inputs = int(input("Enter the number of integers you want to analyze: ")) # Get input

# Get integer values from user
for _ in range(num_inputs): # Loop for user-defined number of inputs
	number = int(input("Enter an integer: "))

	# Check for even or odd using modulo operator
	if number % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
		
print(f"There are {even_count} even numbers and {odd_count} odd numbers.")