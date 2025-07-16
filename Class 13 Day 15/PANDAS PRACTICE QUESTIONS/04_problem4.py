# Q: Add a new column called 'Grade' based on this logic:
# If Marks >= 90 → A
# If Marks >= 80 → B
# Else → C


import pandas as pd
import numpy as np
df = pd.read_csv("students1.csv")
df["Grades"] = np.where(df["Marks"] >= 90 , "A",
                        np.where(df["Marks"] >= 80 , "B","C"))

print(df)