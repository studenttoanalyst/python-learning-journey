class student:
    language = "Punjabi"
    Class = 10
    Age = 19
    name = "Owais"

student = student()
student.language = "Pashto" # instance attribute
student.name = "Asad" # instance attribute
student.Age = 30 # instance attribute
print(student.Age,student.Class,student.name,student.language)

# if an attribute present in object and the same attribute declare in class but their values doesn,t same
# so their is a rule that the value of attribute will print that will be object attribut value

# agar hmary pass class mn or object mn donno attributes same values sy declare hoy hn but
# but unki valuess same na hn tu hmesha instance attribute ki value print hogi