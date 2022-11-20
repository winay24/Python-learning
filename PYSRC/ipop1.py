#----------------------------reading multiple input from cmd at a time
print("enter input of 2 number just like cmd line input : ")
a,b = [int(x) for x in input("enter 2 int val : ").split()]
print("sum  : ",a+b)
#split() return list of string type with values after spliting based on space , int(x) which will type cast