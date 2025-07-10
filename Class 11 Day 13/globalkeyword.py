# GLOBAL KEYWORD
"""global keyword is used to modify the variable outhside of the current scope"""
# global variable wo hota h jisko ap function k ander b use krsakty ho or bahar b use krsakty ho jese..
a = 3 # ye global variable h q k esko hm different functions k ander b use krskty h
def func():
    global a  # ab ye yahan pr global a likhny sy kia hoa essy ye local variable global ban gya h 
    a = 55 # local variable h q k ye sirf function k ander use ho sakta h bahir nh 
    print(a)

func()
print(a)