# Create a pie chart for monthly expenses.

Categories= ['Rent', 'Food', 'Transport', 'Others']
Amounts= [40, 30, 20, 10]
import matplotlib.pyplot as plt
plt.pie(Amounts,labels=Categories)
plt.title("Monthly Expenses")
plt.show()