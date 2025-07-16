# Mini Project using NumPy
# Classroom Marks Analysis
"""
 Situation:
Tu ek teacher hai. Tere paas 5 students ke 4 subjects ke marks hain. Ab tu:
Har student ka total marks
Har student ka average
Sab mein se highest marks
Jis subject mein sabse zyada average aaya
Kaun se student ka result fail hai (agar avg < 33)"""

import numpy as np
marks = np.array([
    [22,34,55,66],
    [66,87,99,55],
    [23,4,5,5],
    [45,66,33,77]
])

# total marks of every student
total_marks = np.sum(marks,axis=1)
print("Total marks of each students is :  ",total_marks)

# Average of every students
Average_marks = np.mean(marks,axis=1)
print("Average marks of each students is :  ",Average_marks)

# Higest marks
Highest_marks = np.max(marks)
print("The highest marks is: ",Highest_marks)

# Subject wise average
subject_avg = np.mean(marks,axis=0)
print("Average marks in each subject: ",subject_avg)

# subject with higest avg
best_sub = np.argmax(subject_avg)
print("Subject with higest avg: Subject",best_sub +1)

# Students who failed
failed_std = np.where(Average_marks<33)[0] +  1
print("Failed std numbers: ",failed_std)