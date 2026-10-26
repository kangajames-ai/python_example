salary = float(input("Please enter your earnings for this year: $"))
yearsOnJob = int(input("Please the number of years you've worked for: "))

if salary >= 30000:
	if yearsOnJob >= 2:
		print("\nCongratulations! You qualify for the loan")
	else:
		print("\nYou did not qualify for the loan")
		print(f" - You've only been at your job for {yearsOnJob} year(s) (minimum 2 years required)")
else:
	print("\nYou did not qualify for the loan")
	print("You must earn at least $30000")
