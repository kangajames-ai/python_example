# Get input from user
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the gallons of gas used: "))
    
# Calculate MPG
mpg = miles_driven / gallons_used
    
# Display result
print(f"\nYour car's fuel efficiency is {mpg:.2f} miles per gallon.")