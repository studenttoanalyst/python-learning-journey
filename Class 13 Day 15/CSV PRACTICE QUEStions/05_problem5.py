import csv

with open("new_students.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row

    max_std = -1
    top_std = None

    for row in reader:
        name = row[0]
        marks = int(row[2])  # Convert marks from string to int
        if marks > max_std:
            max_std = marks
            top_std = name

print("Top student:", top_std, "with", max_std, "marks")
    