vowels = "aeiouAEIOU" # Set of vowel characters (case-insensitive)
vowel_count = 0

text = input("Enter a string: ") # Get input from user

# Check for vowels in each character
for char in text:
	if char in vowels:
		vowel_count += 1
		
print(f"The number of vowels in the string is: {vowel_count}")