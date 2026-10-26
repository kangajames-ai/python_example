# Define constants for readability
START_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214

# Print table headings with clear formatting
print('KPH\t\t\tMPH')
print('-------\t\t\t----')

# Use a for loop to iterate over KPH values
for kph in range(START_SPEED, END_SPEED, INCREMENT):
	# Calculate MPH using the conversion formula
	mph = kph * CONVERSION_FACTOR

	# Print each KPH and MPH value with formatting
	print(f'{kph}\t\t\t{mph:.1f}') # Use f-string for formatting and one decimal place