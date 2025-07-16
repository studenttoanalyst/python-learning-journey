# Bar Chart of Student Marks
# Q: Plot a bar chart showing marks of 4 students.
Names= ['Ali', 'Sara', 'Ahmed', 'Fatima']
Marks= [85, 90, 75, 88]

import matplotlib.pyplot as plt
plt.bar(Names,Marks)
plt.title("Marks of students")
plt.xlabel("Students names")
plt.ylabel("Students marks")
plt.show()