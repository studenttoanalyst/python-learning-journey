# Q: Write the following data into a file "new_students.csv"
# [["Name", "Age", "Marks"],
#  ["Owais", 19, 95],
#  ["Zara", 21, 88]]

import csv
data = [["Name", "Age", "Marks"],
        ["Owais", 19, 95],
        ["Zara", 21, 88]]

# with open("new_students.csv","w") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
with open("new_students.csv","w") as file:
    writer = csv.writer(file)
    writer.writerows(data)