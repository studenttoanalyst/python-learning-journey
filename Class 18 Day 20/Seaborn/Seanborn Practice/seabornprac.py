# # BAR PLOT
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# df = sns.load_dataset("tips")
# sns.barplot(x="day",y="total_bill",data=df)
# plt.title("Average total bill day")
# plt.show()
# 2.	Countplot 
# sns.countplot(x="day",data=df)
# plt.title("Har din kitny customers ay...")
# plt.show()

# # 3.	Boxplot 
# sns.boxplot(x="day",y="total_bill",data=df)
# plt.title("box plot")
# plt.show()
# # 4.	Violinplot
# plt.violinplot(x="day",y="total_bill",data=df)
# plt.title("violine box")
# plt.show()


# #5.	Lineplot
# sns.lineplot(x = "size",y ="tip",data=df) 
# plt.title("Group size k sath tiip ka trend")
# plt.show()

# # 6.	Scatterplot
# sns.scatterplot(x = "total_bill",y = "tip",data=df)
# plt.title("Bill or tip ka relationship")
# plt.show()

# # Heatmap 
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Step 1: Sirf numeric columns lo
# numeric_df = df.select_dtypes(include='number')

# # Step 2: Heatmap banao
# sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
# plt.title("Correlation Matrix")
# plt.show()

