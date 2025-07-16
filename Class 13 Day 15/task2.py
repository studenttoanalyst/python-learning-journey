import pandas as pd
df = pd.read_csv("marks.csv")
filtered = df[df["Science"]>80]
print(filtered)