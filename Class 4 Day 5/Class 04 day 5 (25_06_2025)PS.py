# Q1: Print even numbers from 2 to 10

for i in range(2,11,2):
    print(i)

# Q2: Print numbers from 1 to 5 using while loop
i=1
while(i<=5):
    print(i)
    i+=1

# Q3: Loop through a dictionary and print keys & values
studemt = {"name":"M Owais","age":19,"Class":13}
for key,value in studemt.items():
    print(key,value)   

# Q4:  Print Student Info
student = {
    "name":"asad","age":19,"Grade":"A"
}

for key,value in student.items():
    print(f"{key}___{value}")

# Q Print Subject Marks and Total    
std_marks = {
    "physics":48,"chemistry":55,"Math":90
}
total = 0
for subject,marks in std_marks.items():
    print(f"{subject}___>{marks}")
    total += marks


print("total marks =",total)   

# Update Prices of Products by +10
products = {
    "pen": 50, "pencil": 100,"eraser": 11
}
for items in products:
    products[items] += 10

print(products)    

# Q Print Subject Marks and Total  

college_marks = {
    "english":70,"maths":99,"ict":66
}
total = 0
for subjects,marks in college_marks.items():
    total += marks
    print(college_marks)

print("total marks:",total)   

# Find Highest Marks in Subjects
marks11 = {
    "english": 11,
    "urdu": 33,
    "maths" : 90
}
highest = 0
top_subject = ""

for subject,score in marks11.items():
    if(score>highest):
        highest = score
        top_subject = subject
print(f"{highest} in {top_subject}")        
