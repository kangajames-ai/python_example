TAX_FACTOR = 0.0065

# Get the first lot number (or sentinel to end)
print('Enter the property lot number or enter 0 to end.')
lot = int(input('Lot number: '))

# Loop until the sentinel value (0) is entered
while lot != 0:
	# Get property value
	value = float(input('Enter the property value: '))

	# Calculate tax
	tax = value * TAX_FACTOR

	# Display tax
	print(f'Property tax: ${tax:,.2f}') # Formatted output with comma separator and two decimal places

	# Get the next lot number (or sentinel)
	print('Enter the next lot number or enter 0 to end.')
	lot = int(input('Lot number: '))