# write aprogram to generate multiplication tables from 2 to 20 and write it to the different files.
# place these files in a folder for a 13 years old boy

def generat_tables(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"tables111/tableno{n}","w") as file:
        file.write(table)
    for n in range(2,21):
        generat_tables(n)
print("generated 3333")





























# # def generatetable(n):
# #     table = ""
# #     for i in range(1,11):
# #         table += f"{n} X {i} = {n*i}\n"

# #     with open(f"tables/table{n}.txt","w") as file:
# #         file.write(table)
# # for num in range(2, 21):
# #     generatetable(num)

# # print("All tables from 2 to 20 have been generated in the 'tables' folder.")    

# # def generatetable(n):
# #     table = ""
# #     for i in range(1,11):
# #         table += f"{n} X {i} = {n*i}\n"
# #     with open(f"tables/table{n}.txt","w") as file:
# #         file.write(table)
# # for num in range(2,21):
# #     generatetable(num)

# # print("All tables from 2 to 20 have been generated in the 'tables' folder.")

# # def generatetable(n):
# #     table = ""
# #     for i in range(1,11):
# #         table += f"{n} X {i} = {n*i}\n"
# #     with open(f"tables/table{n}.txt","w") as file:
# #         file.write(table)

# # for n in range(2,21):
# #     generatetable(n)

# # print("All Tables from 2 to 21 have been generated in 'tables' folder")

# def generatetable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"
#     with open(f"Collectionoftables/table{n}.txt","w") as file:
#         file.write(table)
# for num in range(2,21):
#     generatetable(num)

# print("All generated tables from 2 to 20 are available in tables folder")