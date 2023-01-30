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
total = 0
customer_id_list = []

for line in sales_csv:
    if customer_id_list == []:
        customer_id_list.append(line[0])

    if line[0] not in customer_id_list:
        total = format(total, ".2f")
        sales_report_csv.writerow([customer_id_list[-1], total])
        customer_id_list.append(line[0])
        total = 0
        total += float(line[3]) + float(line[4]) + float(line[5])
    elif line[0] in customer_id_list:
        total += float(line[3]) + float(line[4]) + float(line[5])

sales_report_csv.writerow([customer_id_list[-1], total])

# Close both files
sales.close()
sales_report.close()
