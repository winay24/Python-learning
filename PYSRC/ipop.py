#Raw input functio  always takes input as string only
#x = raw-input("enter input value : ") upto only python2.x not there in 3
#input function in 2.x is not same as 3.x 
#python 3 input() acts as raw_input()
x = input("enter some value : ")
print(type(x))
#should be type casted if we want other datatypes as input

#-----------------------------------------input()
a = int(input("enter value 1 : "))
b = int(input("enter value 2 : "))
print("sum of val1 + val2 : ",a+b)
print("printing single line cmd output : ")
print("sum  is : ",int(input("enter va1 :"))+int(input("enter va2 :")))

#-----------------------------------------reading and printing employee data
print("started employee program here : ")
eno = int(input("enter employee no : "))
ename = input("enter employee name : ")
esal = float(input("enter employee salary : "))
eloc = input("enter city : ")
#emaried = bool(input("enter ANYVALUE for married ENTER for not married : "))
emaried = eval(input("enter TRUE for married FALSE for not married : "))

print("EMP data : ")
print(eno)
print(ename)
print(esal)
print(eloc)
print("marriage status : ",emaried)

#in above example have we have one problem taking input for bool function for that we have evaluie function

