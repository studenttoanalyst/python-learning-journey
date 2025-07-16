# # Example bar chart
# import matplotlib.pyplot as plt

# x = ['Math', 'Science', 'English']
# y = [80, 70, 90]

# plt.bar(x, y)  # Use x and y here
# plt.title("Student Marks")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()

# # example pie chart
# import matplotlib.pyplot as plt

# labels = ['Apple', 'Banana', 'Mango']
# sizes = [30, 45, 25]

# # plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# # plt.title("Fruit Popularity")
# # plt.show()

# explode = (0, 0.1, 0)  # "explode" Banana slice
# colors = ['#ff9999','#66b3ff','#99ff99']

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, colors=colors)
# plt.title("Fruit Popularity 🍎🍌🥭")
# plt.show()

# #  Example 3: Scatter Plot
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 12, 20, 25, 30]

# plt.scatter(x, y)
# plt.title("My Scatter Plot")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.show()


# bar chart
# import matplotlib.pyplot as plt
# x = ["Calculas","DMS","ICT","PF","English"]
# y = [92,68,61,62,77]
# plt.bar(x,y)
# plt.title("Student marks")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()

# pie chart
import matplotlib.pyplot as plt
Subjects= ["Calculas","DMS","ICT","PF","English"]
Marks = [92,68,61,62,77]
plt.pie(Marks, labels=Subjects,autopct="%1.1f%%")
plt.title("Student ma()rks")
plt.show()

# scatter 
# import matplotlib.pyplot as plt
# Subjects= ["Calculas","DMS","ICT","PF","English"]
# Marks = [92,68,61,62,77]

# plt.scatter(Subjects,Marks)
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()