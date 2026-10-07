# Enter the principle amount and years to maturity
principle = float(input("Enter the principle amount: $"))
years = int(input("Enter the years to maturity: "))

# Determine the interest rate
if principle > 100000 and years == 5:
    interest_rate = 0.06
elif 50000 <= principle <= 100000 and years == 10:
    interest_rate = 0.05
elif 50000 <= principle <= 100000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

# Calculate first-year interest
interest_amount = principle * interest_rate

# Display the results with decimals aligned
print()
print(f"{'Principle:':<25}${principle:>12,.2f}")
print(f"{'Interest rate:':<25}{interest_rate:>13.2%}")
print(f"{'First-year interest:':<25}${interest_amount:>12,.2f}")
