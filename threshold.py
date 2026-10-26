# Set the threshold temperature
threshold = 25

# Initialize the temperature variable
temperature = 0

# Continuously monitor the temperature until it's safe
while temperature <= threshold:
	# Simulate getting the current temperature
	temperature = float(input("Enter the current temperature: "))

	# Check if the temperature exceeds the threshold
	if temperature > threshold:
		print("Temperature exceeds safe levels! Sound the alarm!")
	else:
		print("Temperature is within safe levels.")
		
print("End of temperature monitoring.")
