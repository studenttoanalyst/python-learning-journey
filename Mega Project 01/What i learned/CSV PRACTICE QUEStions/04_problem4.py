# Q: Count how many students are in "students.csv" (excluding header)
import csv

with open("students.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    count = sum(1 for row in reader) # count remaining rows
    print("Total students: ", count)
