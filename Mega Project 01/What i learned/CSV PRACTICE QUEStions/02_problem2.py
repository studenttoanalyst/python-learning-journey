# # Q: Print only the 'Name' column from students.csv
# File Example:
# Name,Age,Marks
# Ali,18,85
# Sara,20,90

# import csv

# with open("students.csv") as f:
#     reader = csv.reader(f)
#     for column in reader:
#         print(column[0])

# Code to print only the first row:
# import csv

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     first_row = next(reader)
#     print(first_row)

# Code to print only the second  row:
 
# import csv

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     first_row = next(reader)
#     second_row= next(reader)
#     print(second_row)

import csv
with open("students.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[0])