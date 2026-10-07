# Get the quantity of widgets
quantity = int(input("Enter the quantity of widgets: "))

# Determine the price per widget
if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
    price = 20.00
else:
    price = 30.00

# Calculate extended price, tax, and total
extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

# Display the results with decimal places aligned
print()
print(f"{'Price per widget:':<20} ${price:>10.2f}")
print(f"{'Extended price:':<20} ${extended_price:>10.2f}")
print(f"{'Tax (7%):':<20} ${tax:>10.2f}")
print(f"{'Total:':<20} ${total:>10.2f}")