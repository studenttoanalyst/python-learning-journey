# write a program to find out the line number where python is present from question 7

with open("log.txt") as file:
    lines = file.readlines()
lineno =1
for line in lines:
  if("python" in line):
    print(f"Yes python is available in line no {lineno}")
    break
  lineno += 1

else:
    print("No python is not available")