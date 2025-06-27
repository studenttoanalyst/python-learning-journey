# mini project : Order online summary
"""Store customer details in a dictionary
Keep track of items ordered using a set
Update total bill (no loops!)
Add, remove, and display data using direct dictionary and set operations
"""
# ________________________________________________________________________________

customer_details = {
    "Name"      : "Faizan Ali",
    "Phone"     : "0321_2887035",
    "Gmail"     : "abc@gmail.com",
    "Total_bill": 0

} 

ordered_item = set()
ordered_item.add("Mobile")
ordered_item.add("HeadPhones")
ordered_item.add("Charger")
ordered_item.add("Laptop")

customer_details["Total_bill"] += 10000  # Mobile price
customer_details["Total_bill"] += 5000  # HeadPhones price
customer_details["Total_bill"] += 2000  # Charger price
customer_details["Total_bill"] += 50000  # Laptop price

ordered_item.remove("HeadPhones")
customer_details["Total_bill"] -= 5000  #  update HeadPhones price

ordered_item.remove("Laptop")
customer_details["Total_bill"] -= 50000  # update Laptop price


print("Customer",customer_details["Name"])
print("Phone",customer_details["Phone"])
print("Gmail",customer_details["Gmail"])
print("Total Items",ordered_item)
print("Tptal bill",customer_details["Total_bill"])



# Mini Project: Student Grading System
"""Objective:
You have one student. Based on their marks in 3 subjects, calculate:
Total marks
Percentage
Grade:
A: ≥ 90%
B: ≥ 80%
C: ≥ 70%
D: ≥ 60%
F: < 60%
"""
# ___________________________________________________________________

Student_name = "Talha"
subject1 = 88
subject2 = 70
subject3 = 50
total_Marks = 300
obtained_Marks = 88+70+50
percentage = (obtained_Marks/total_Marks)*100
if(percentage>=90):
    print("\nYour Grade is A")
elif(percentage>=80):
    print("\nYour Grade is B")    
elif(percentage>=70):
    print("\nYour Grade is C")    
elif(percentage>=60):
    print("\nYour Grade is D")    
else:
    print("\nFail")    