# Multiple Line Graphs
# Q: Plot two lines: one for boys' marks, one for girls'.
Subjects= ['Math', 'Science', 'English']
Boys= [70, 75, 80]
Girls= [85, 80, 90]

import matplotlib.pyplot as plt
subjects = ['Math', 'Science', 'English']
boys = [70, 75, 80]
girls = [85, 80, 90]

plt.plot(subjects, boys, label="Boys")
plt.plot(subjects, girls, label="Girls")
plt.title("Marks Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.show()

