# Get the purchase amount from the user
purchase_amount = float(input("Enter the amount of the purchase: $"))

# Define tax rates
STATE_TAX_RATE = 0.04  # 4%
COUNTY_TAX_RATE = 0.02  # 2%
    
# Calculate taxes
state_tax = purchase_amount * STATE_TAX_RATE
county_tax = purchase_amount * COUNTY_TAX_RATE
total_tax = state_tax + county_tax
total_sale = purchase_amount + total_tax
    
# Display results
print("\nPurchase Details:")
print(f"Purchase Amount: ${purchase_amount:.2f}")
print(f"State Sales Tax (4%): ${state_tax:.2f}")
print(f"County Sales Tax (2%): ${county_tax:.2f}")
print(f"Total Sales Tax: ${total_tax:.2f}")
print(f"Total Sale Amount: ${total_sale:.2f}")