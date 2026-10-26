# Software Package Purchase Calculator

# Constants
PACKAGE_PRICE = 105  # Price per package in Leones

# Get user input
quantity = int(input("Enter the number of packages purchased: "))

# Calculate discount based on quantity
if quantity >= 70:
    discount_percent = 50
elif quantity >= 30:
    discount_percent = 30
elif quantity >= 11:
    discount_percent = 15
elif quantity >= 5:
    discount_percent = 5
else:
    discount_percent = 0

# Calculate amounts
subtotal = quantity * PACKAGE_PRICE
discount_amount = subtotal * discount_percent / 100
total = subtotal - discount_amount

# Display results
print(f"\nNumber of packages: {quantity}")
print(f"Discount applied: {discount_percent}%")
print(f"Discount amount: Le{discount_amount:,.2f}")
print(f"Total amount after discount: Le{total:,.2f}")