# Import CSV library
import csv

# Open sales.csv file and read it as a csv file
sales = open("sales.csv", "r")
sales_csv = csv.reader(sales, delimiter=",")

# Skip the header
next(sales_csv)

# Create a new csv file and add header
sales_report = open("salesreport.csv", "w")
sales_report_csv = csv.writer(sales_report, delimiter=",")
sales_report_csv.writerow(["CustomerID", "Total"])

# Read CustomerID, SubTotal, TaxAmt, and Freight, calculate Total, and write it to salesreport.csv
for line in sales_csv:
    total = format((float(line[3]) + float(line[4]) + float(line[5])), ".2f")
    sales_report_csv.writerow([line[0], total])

# Close both files
sales.close()
sales_report.close()
