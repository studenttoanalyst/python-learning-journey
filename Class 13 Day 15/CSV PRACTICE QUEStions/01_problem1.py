# Read and Print All Rows
# # Q: Read a CSV file named "students.csv" and print all rows.
# import csv

# with open("students.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#      print(row)

# import pandas as pd

# df = pd.read_csv("students.csv")
# print(df)

import csv 
with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)