# Q: Show only those students who got more than 85 marks

import pandas as pd
df = pd.read_csv("students1.csv")
highest = df[df["Marks"]>85]
print(highest)
