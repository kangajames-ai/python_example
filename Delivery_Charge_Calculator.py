# Delivery Charge Calculator

# Get user input
weight = float(input("Enter package weight in kg: "))
distance = float(input("Enter delivery distance in km: "))

# Calculate delivery charges
if weight > 10:
    if distance > 100:
        charge = weight * 12
    else:
        charge = weight * 6
else:
    if distance > 50:
        charge = weight * 8
    else:
        charge = weight * 4

# Display result
print(f"\nDelivery charge: Le{charge:,.2f}")