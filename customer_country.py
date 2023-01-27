# Import CSV library
import csv

# Open customers.csv file and read it as csv file
infile = open("customers.csv", "r")
infile_csv = csv.reader(infile, delimiter=",")

# Create customer_country.csv and add header
outfile = open("customer_country.csv", "w")
outfile_csv = csv.writer(outfile, delimiter=",")
outfile_csv.writerow(["Name", "Country"])

# Skip header for infile_csv
next(infile_csv)

# Write First Name, Last Name, and Country from infile_csv to outfile_csv
for line in infile_csv:
    outfile_csv.writerow([(line[1] + " " + line[2]), line[4]])

# Close both files
infile.close()
outfile.close()
