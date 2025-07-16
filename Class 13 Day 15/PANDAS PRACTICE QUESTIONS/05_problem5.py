# Q: Save the DataFrame with grades to a new file: "graded_students.csv"
import pandas as pd
import numpy as np
df = pd.read_csv("students1.csv")
df["Grades"] = np.where(df["Marks"] >= 90 , "A",
                        np.where(df["Marks"] >= 80 , "B","C"))
df.to_csv("graded_std.csv",index=False)
print("FIle saved!!!!!!!")