
import csv 
from datetime import datetime

now = datetime.now()
date = now.strftime("%Y-%m-%d")
time  = now.strftime("%H-%M-%S")
day = now.strftime("%A")
try:
    category = str(input("Enter category:  "))
except ValueError:
    print("invalid category!")
    exit()
    
try:
    amount = float(input("Enter category amount:  "))
except ValueError:
    print("Amount must be a number!")
    exit()

try:
    entry_type = input("Enter type(Expense or Income):  ").capitalize()
    if entry_type not in (["Expense","Income"]):
        print("Type must be in Expense or in Income!!!")
        exit()
except ValueError:
    print("Invalid type!!!")
    exit()

with open("data.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([date,day,time,category,amount,entry_type])

print("Data successfully entered!!!!!!")
try:
    import pandas as pd
    df = pd.read_csv("data.csv")
    df.columns = ["Date", "Day", "Time", "Category", "Amount", "entry_type"]

    
    print(df)
except:
    print("File not found!!!")

try:
   
    total_income = df[df["entry_type"] == "Income"]["Amount"].sum()
    total_expense = df[df["entry_type"] == "Expense"]["Amount"].sum()
    net_savings = total_income - total_expense


    print("\nAnalysis summary:")
    print("Total income:  Rs",total_income)
    print("Total expense: Rs",total_expense)
    print("Total savings: Rs",net_savings)
except FileNotFoundError:
    print("File not found!!!!")


# import csv
# from datetime import datetime
# now = datetime.now()
# Day = now.strftime("%A")
# Date = now.strftime("%Y-%m-%d")
# Time = now.strftime("%H:%M:%S")

# Category = input("Enter category:  ")
# try:
#  Amount = float(input("Enter the amount of category:  "))
# except ValueError:
#  print("invaled amount!!!!")
#  exit()
# try:
#  Enter_Type  = input("Type(Expense or Income): ").capitalize()
#  if Enter_Type not in (["Expense","Income"]):
#   print("Type must be in Income or Expense!!!!")
# except ValueError:
#  print("Invalid type!!!!")
#  exit()

# # with open("data2.csv", "w", newline="") as file:
# #     writer = csv.writer(file)
# #     writer.writerow(["Date", "Day", "Time", "Category", "Amount", "Enter_Type"])

# # print("✅ Header added successfully to new file!")
# with open("data2.csv","a") as file:
#  writer = csv.writer(file)
#  writer.writerow([Date,Day,Time,Category,Amount,Enter_Type])

# print("Data succesfully entered!!!")
# try:
#     import pandas as pd
#     df = pd.read_csv("data2.csv")
#     df.columns = ["Date", "Day", "Time", "Category", "Amount", "Enter_Type"]
#     print(df)
# except FileNotFoundError:
#   print("file not found!!!!")

# try:
#   total_income = df[df["Enter_Type"]=="Income"]["Amount"].sum()
#   total_expense = df[df["Enter_Type"]=="Expense"]["Amount"].sum()
#   net_savings = total_income - total_expense
#   print("\nAnalysis summary")
#   print("Total Expense:  ",total_expense)
#   print("Total Income:  ",total_income)
#   print("Total Sabings:  ",net_savings)
# except ValueError:
#   print("Something went")

# import csv
# from datetime import datetime

# date = datetime.now().strftime("%Y-%m-%d")
# time = datetime.now()
# category =  input("Kis cheez ka kharcha/income h? (eg:Food,salary):  ")
# amount =  float(input("kitna paisy?(e.g: 500):  "))
# entry_type =  input("ye income h ya expense h?:  ")

# with open("data.csv","a") as file:
#     writer = csv.writer(file)
#     writer.writerow([date, category, amount, entry_type])
# print("record save hogaya h data.csv file m!!!!!!!!!!!  ")

# import pandas as pd
# df = pd.read_csv("data.csv")
# print(df)

# import csv
# from datetime import datetime 
# now = datetime.now()
# date = now.strftime("%Y-%m-%d")
# day = now.strftime("%A")     
# time = now.strftime("%H-%M-%S") 

# category = input("Enter category (e.g: salary,food,toys etc): ")
# amount = float(input("Enter amount of category:   "))
# entry_type = input("Expense or income?:  ")

# with open("data.csv","a") as file:
#     writer = csv.writer(file)
#     writer.writerow([date, day, time, category, amount, entry_type])

# print("Data succesfully entered!!!!!!!!!!")

# import pandas as pd
# df = pd.read_csv("data.csv")

# print(df)