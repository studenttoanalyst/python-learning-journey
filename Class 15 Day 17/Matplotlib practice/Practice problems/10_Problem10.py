# Customize Line with Color & Style
# Q: Draw a dotted red line chart of prices.
Days= [1, 2, 3, 4]
Price= [100, 105, 102, 108]
import matplotlib.pyplot as plt
plt.plot(Days, Price, 'r--')  # r = red, -- = dotted
plt.title("Price Trend")
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()