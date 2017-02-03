print("This program determines the weekly salary for an employee.")
print("The salary is the sum of the hourly rate times the \nhours worked, plus the bonus.")
print("For work hours exceeding 40 per week, an overtime rate \nof 1.5 is applied.")
print("The user must indicate if the worker has received a \nbonus by answering a y/n question.")
print("Input consists of: hours worked, hourly rate, bonus.")
print("The output is the total salary for this week.\n")

hours_worked = float(input("Enter the number of hours worked this week: "))
rate_per_hour = float(input("Enter the salary rate per hour (please do not include the '$' sign): "))
yes_no = input("Did the worker get a bonus? (y/n): ")

if yes_no == 'y':
    bonus = float(input("Enter the bonus amount: "))
else:
    bonus = 0

if hours_worked > 40:
    overtime = (hours_worked - 40) * rate_per_hour * 1.5
    non_overtime = 40 * rate_per_hour
    salary = non_overtime + overtime + bonus
else:
    overtime = 0
    non_overtime = hours_worked * rate_per_hour
    salary = non_overtime + bonus

overtime = "{0:.2f}".format(overtime)
salary = "{0:.2f}".format(salary)
print("The total salary for the worker $" + salary + " (overtime pay is $" + overtime + ")")

