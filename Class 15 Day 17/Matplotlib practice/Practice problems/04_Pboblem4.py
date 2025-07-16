# Show the relationship between age and salary using a scatter plot.
Age = [22, 25, 30, 35, 40]
Salary = [25, 35, 50, 65, 80]
import matplotlib.pyplot as plt
plt.scatter(Age,Salary)
plt.title("Relationship b/w age and salary")
plt.xlabel("Age")
plt.ylabel("sALARY")
plt.show()