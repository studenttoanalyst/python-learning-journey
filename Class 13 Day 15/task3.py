import pandas as pd
import numpy as np
df = pd.read_csv("marks.csv")
df["Average"] = (df["Maths"] + df["English"] + df["Science"])/3
print(df)
df["Result"] = np.where(df["Average"]>= 60,"Pass","Fail")
print(df)

print(df["Result"].value_counts())
print(df["Result"].value_counts())
