#operator only applicable for one operand then unary , 2 binay op, 3 or more is ternary
#also called conditional oper
a = 10
b = 20
#c = a>b ? 30 : 40 in c prog
c = 30 if a<b else 40
print("ternary o/p : ",c)

#sample program to find max value
x = int(input("enter integer1 : "))
y = int(input("enter integer2 : "))
max = x if x>y else y
print("max value is : ",max)