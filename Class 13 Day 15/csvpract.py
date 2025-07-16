import csv

# with open("data.csv", "r") as f:
#     reader = csv.reader(f)
#     for colum in reader:
#         print(colum)

# import pandas as pd

# df = pd.read_csv("data.csv")
# print(df)

data = [
    ["Name","Age","city"],
    ["OWAIS","21","karachi"],
    ["ANUS","22","lahore"],
    ["ALI","11","Islamabad"],
]
with open("new_data.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)