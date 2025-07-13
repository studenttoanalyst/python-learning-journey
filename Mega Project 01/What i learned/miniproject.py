# Student Result Management System
# Project Goals:
# We'll perform the following steps using Pandas:

# Read the data from CSV

# Calculate Total Marks and Percentage

# Assign Grades based on percentage

# Filter students with grades A, B, C

# Find Topper

# Save updated results into a new CSV file



# 1)_Read the data from CSV
import pandas as pn
import numpy as np
df = pn.read_csv("students.csv")


# 2)_Calculate Total Marks and Percentage

df["Total"] = df["Maths"] + df["English"] + df["Science"]
df["Percentage"] = df["Total"]/3

# 3)_Assign Grades
df["Grades"] = np.where(df["Percentage"]>=90,"A",
                np.where(df["Percentage"]>=80,"B",
                np.where(df["Percentage"]>=70,"C","Fail")) )

# 4)_Filter students with grades A, B, C
grade_A = df[df["Grades"] == "A"]
grade_B = df[df["Grades"] == "B"]
grade_C = df[df["Grades"] == "C"]
failures = df[df["Grades"] == "Fail"]

# 5)_Find Topper

topper = df[df["Percentage"] == df["Percentage"].max()]

# 6)_Save updated results into a new CSV file
df.to_csv("final_results.csv",index=False)

# print output
print("Full result: ",df)
print("\nTopper: ",topper)