# Horizontal Bar Chart
# Q: Show horizontal bars of different product quantities.
Products= ['A', 'B', 'C']
Quantity= [40, 60, 30]
import matplotlib.pyplot as plt
plt.barh(Products,Quantity)
plt.title("Horizontal bar graph")
plt.xlabel("Quantity")
plt.ylabel("Products")
plt.show()