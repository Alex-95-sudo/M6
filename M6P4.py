# Enter the number of concert tickets
tickets = int(input("Enter the number of concert tickets: "))

# Determine the price per ticket
if tickets >= 25:
    price_per_ticket = 50.00
elif tickets >= 10:
    price_per_ticket = 60.00
elif tickets >= 5:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00

# Calculate total cost
total_cost = tickets * price_per_ticket

# Display the results
print()
print(f"{'Number of tickets:':<25}{tickets:>10}")
print(f"{'Price per ticket:':<25}${price_per_ticket:>9.2f}")
print(f"{'Total cost:':<25}${total_cost:>9.2f}")