# Enter employee information
last_name = input("Enter employee last name: ")
salary = float(input("Enter employee salary: $"))
job_level = int(input("Enter job level: "))

# Determine the bonus rate
if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

# Calculate bonus
bonus = salary * bonus_rate

# Display the results with decimals aligned in columns
print()
print(f"{'Employee last name:':<25}{last_name:>12}")
print(f"{'Bonus:':<25}${bonus:>11,.2f}")