# Bar Chart with Colors
# Q: Show colored bars for sales in different cities.
Cities= ['Karachi', 'Lahore', 'Islamabad']
Sales= [200, 150, 180]
color = ["red","blue","green"]
import matplotlib.pyplot as plt
plt.bar(Cities,Sales,color = color)
plt.title("City sales")
plt.xlabel("Cities")
plt.ylabel("Sales")
plt.show()