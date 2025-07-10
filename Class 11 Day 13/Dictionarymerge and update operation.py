# DICTIONARY MERGE AND UPDATE OPERATION 
a = {
    "name" : "owais",
    "age"  : 12
}
b = {
    "city" : "Karachi",
    "Goal" : "Paisa"
}

c = a|b
print(c)   # a and b are merged into a new dictionary c   (Original a and b stay unchanged)

