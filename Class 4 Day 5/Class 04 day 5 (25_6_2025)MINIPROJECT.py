# Project Description
"""You are building a report card system for 3 students.
Each student has:
A name
A dictionary of subject marks
Calculated:
Total marks
Percentage
Grade
A final report printed"""



students = {
    "owais":{"english":33,"maths":55,"islamiat":22},
    "asad":{"english":33,"maths":55,"islamiat":22},
    "ali":{"english":33,"maths":55,"islamiat":22}
    
}
subject_set = set()
for name,marks in students.items():
    total = 0
    print(f"\n_____________________report for {name}")
    for subject,score in marks.items():
        print(f"{subject}_______{score}")
        total += score 
        subject_set.add(subject)
        percentage = total/len(marks)

        if(percentage>=90):
            grade = "A"
        elif(percentage>=80):
            grade = "B"
        elif(percentage>=70):
            grade = "C"
        elif(percentage>=60):
            grade = "D"
        else:
            grade = "F"
        
        print(f"total score : {total}")
        print(f"percentage : {percentage}")
        print(f"grade : {grade}")

print("\nAll unique Subjects: ",subject_set)






























# step 01 student data 
# students = {
#     "owais":{"english":44,"maths":99,"computer":77},
#     "afaq":{"english":87,"maths":76,"computer":12},
#     "usman":{"english":32,"maths":98,"computer":33}
# }

# # # step 02 to tract unique subjects
# # subjects_set = set()
# # # loop throw each subject
# # for name,marks in students.items():
# #     total = 0
# #     print(f"\n____________________Report Card for {name}______")

# #     # add subjects to set and calculate total
# #     for subject,score in marks.items():
# #         subjects_set.add(subject)
# #         print(f"{subject}: {score}")
# #         total += score
# #         percentage = total/len(marks)

# #         # grade logic
# #         if(percentage>=90):
# #             grade = "A"
# #         elif(percentage>=80):
# #             grade = "B"
# #         elif(percentage>=70):
# #             grade = "C"
# #         elif(percentage>=60):
# #             grade = "D"
# #         else:
# #             grade = "F" 

# subjects_set = set()
# for name,marks in students.items():
#     total = 0
#     print(f"\n_____________Report for {name}")
#     for subject,score in marks.items():
#         subjects_set.add(subject)
#         print(f"{subject}: {score}")
#         total += score
#         percentage = total/len(marks)

#         if(percentage>=90):
#             grade = "A"
#         elif(percentage>=80):
#             grade = "B"
#         elif(percentage>=70):
#             grade = "C"
#         elif(percentage>=60):
#             grade = "D"
#         else:
#             grade = "F"


#         print(f"TOTAL = {total}")
#         print(f"Your percentage is :{percentage} ")
#         print(f"grade: {grade}")    

