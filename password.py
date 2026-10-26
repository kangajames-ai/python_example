# Set the correct password
correct_password = "abc123"

# Initialize the entered password variable
entered_password = ""

# Continuously prompt the user for their password until it's correct
while entered_password != correct_password:
	entered_password = input("Enter your password: ")

	# Check if the entered password matches the correct one
	if entered_password != correct_password:
		print("Incorrect password. Please try again.")
		
print("Login successful. Welcome to your account!")