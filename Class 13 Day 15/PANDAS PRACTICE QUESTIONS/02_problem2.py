# Q: From the DataFrame, show only the 'Name' and 'Marks' columns
import pandas as pd
df = pd.read_csv("students1.csv")
print(df[["Name","Marks"]])