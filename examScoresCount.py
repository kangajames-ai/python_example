sentinel_score = -1 # Sentinel value to indicate the end of scores
total_score = 0
num_students = 0

# Get exam scores until the sentinel value is entered
score = float(input("Enter an exam score (or -1 to end): "))
while score != sentinel_score:
	total_score += score
	num_students += 1

	# Get the next score (or sentinel)
	score = float(input("Enter an exam score (or -1 to end): "))

# Calculate and display average (avoid division by zero)
if num_students > 0:
	average_score = total_score / num_students
	print(f"The average score for {num_students} students is: {average_score:.2f}")
else:
	print("No scores were entered.")