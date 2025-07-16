# Project: Student Performance Report
import pandas as pd
data = []
while True:
    name  = input("Enter student name or type exit to finish: ").capitalize()
    if name == "Exit"  :
        break
        
    subject = input("Enter Subject: ").capitalize()
    try:
     marks = int(input("Enter marks: "))
     if marks > 100:
        print("❌ Invalid marks! Marks cannot be more than 100.")
        exit()
    except ValueError:
     print("❌ Invalid input! Marks must be a number.")
     exit()
 
        
    try:
    
     attendance = int(input("attendence (%): "))
     if attendance > 100:
        print("❌ Invalid attendence! attendence cannot be more than 100.")
        exit()
    except ValueError:
        print("Invalid attendence!!")
        exit()
    data.append({
        "Name" : name,
        "Subject": subject,
        "Marks" : marks,
        "Attendance": attendance
    })
if len(data)>0:
        df = pd.DataFrame(data)
        df.to_csv("students1.csv",index=False)
        print("\nData saved successfully!!!")

        avg_marks = df.groupby("Name")["Marks"].mean().reset_index()
        print(avg_marks)

        low_marks = df[df["Marks"]<70]
        print("Students with Low score:  ")
        print(low_marks)

        def get_grades(Marks):
            if Marks >= 90:
                return "A"
            elif Marks >= 80:
                return "B"
            elif Marks >= 70:
                return "C"
            else:
                return "D"

        df["Grade"] = df["Marks"].apply(get_grades)
        print(df[["Name","Marks","Grade"]])

        low_attendance = df[df["Attendance"] < 75]
        print("Low Attendance Students:")
        print(low_attendance)
else:
     print("\n⚠️ No student data entered. Nothing saved.")

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 10))
plt.bar(avg_marks["Name"], avg_marks["Marks"], color='darkblue')
plt.title("📊 Average Marks by Student")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

