# Import csv library
import csv

# Open EmployeePay.csv and read it as csv file
employee = open("EmployeePay.csv", "r")
employee_csv = csv.reader(employee, delimiter=",")

# Skip the header
next(employee_csv)

# Print out each employee's information
for record in employee_csv:
    print(f"Here is the information for {record[1]} {record[2]}:")
    print(f"The employee's ID is {record[0]}.")
    print(f"The employee's salary is {record[3]}.")
    print(f"The employee's bonus percent is {record[4]}")
    bonus = format((float(record[3]) * float(record[4])), ".2f")
    print(f"The employee's bonus amount is {bonus}")

# Close the file
employee.close()
