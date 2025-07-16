# Q: Show the average, max, and min marks of all students using one-liners ?
import pandas as pd
df = pd.read_csv("students1.csv")
print("Average: ",df["Marks"].mean())
print("Minimum: ",df["Marks"].min())
print("Maximum: ",df["Marks"].max())