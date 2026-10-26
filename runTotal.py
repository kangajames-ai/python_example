MAX_NUMBERS = 5 # Maximum number of numbers to accept

total = 0.0 # Initialize accumulator to 0

print('This program calculates the sum of', MAX_NUMBERS, 'numbers you will enter.')

# Get the numbers and accumulate them
for counter in range(MAX_NUMBERS):
	number = float(input('Enter a number: '))
	total += number # Same as total = total + number

# Display the total
print(f'The total is {total}.')