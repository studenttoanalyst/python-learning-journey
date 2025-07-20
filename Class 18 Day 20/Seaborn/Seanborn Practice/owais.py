import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")  # Load your CSV file
# print(df.head(6))               # Print first 5 rows of the dataframe

# df_sunday = df[df['day'] == 'Sun']
# print(df_sunday.head())

# sns.barplot(x ="sex",y="tip",data=df_sunday)
# plt.title("Average tip by gender on sunday")
# plt.show()

# # Sirf Female customers:
# female_customers = df[df["sex"]=="Female"]
# print(female_customers)

# sns.barplot(x="sex",y="tip",data=female_customers)
# plt.title("Female customers")
# plt.show()


# # sirf smokers
# df_smokers = df[df["smoker"]=="No"]
# print(df_smokers)

# sns.countplot(x="smoker",data=df_smokers)
# plt.title("Smokers available?")
# plt.show()

# Sirf Dinner time wale customers:
# df_dinnertime = df[df["time"]=="Dinner"]
# print(df_dinnertime)

# sns.countplot(x = "time",data=df_dinnertime)
# plt.title("Dinner time cus")
# plt.show()

# Customers jinki total_bill 20 se zyada ho:

df_totalbill = df[df["total_bill"]>20]
print(df_totalbill)
sns.histplot(data=df_totalbill, x="total_bill", bins=10, kde=True)
plt.title("Distribution of Total Bills > $20")
plt.show()
