
# HEADER: Learning List, sum and range
# when?: You'd use list when ordered colection of same-type items like tags on blog to filter blog post type.

total = 0
expenses = []
num_expenses = int(input("Enter a # of expenses:"))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)


print("You spent $", total, sep= '')


