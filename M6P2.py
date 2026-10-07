# Enter part number and quantity
part_number = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))

# Determine the unit cost
if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

# Calculate total cost
total_cost = quantity * unit_cost

# Display the results with decimals aligned in columns
print()
print(f"{'Part number:':<20}{part_number:>10}")
print(f"{'Cost per unit:':<20}${unit_cost:>9.2f}")
print(f"{'Total cost:':<20}${total_cost:>9.2f}")