# Import CSV library
import csv

# Open customers.csv file and read it as csv file
infile = open("customers.csv", "r")
# infile_csv = csv.reader(infile, delimiter=",")

# Create customer_country.csv and add header
outfile = open("customer_country.csv", "w")
# outfile_csv = csv.writer(outfile, delimiter=",")
outfile.write("Name" + "," + "Country" + "\n")

# Skip header for infile_csv
next(infile)

# Write First Name, Last Name, and Country from infile_csv to outfile_csv
for line in infile:
    line_list = line.split(",")
    outfile.write(line_list[1] + " " + line_list[2] + "," + line_list[4] + "\n")

# Close both files
infile.close()
outfile.close()
