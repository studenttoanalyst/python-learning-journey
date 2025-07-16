# Q: Plot a line chart showing temperature over 5 days.

import matplotlib.pyplot as plt


Days =  ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
Temperature = [30, 32, 33, 31, 29]

plt.plot(Days,Temperature)
plt.title("Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

