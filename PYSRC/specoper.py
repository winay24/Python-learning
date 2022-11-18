#identity operator : "is" and "is not"    a is b true whne both are pointing to same address
a = 10
b = 10
print("a is b : ", a is b) #true because integer
l1 = [10,20,30]
l2 = [10,20,30]
print("l1 is l2 : ", l1 is l2) #false because list
print(l1 == l2)  #equality true

#-----------------------membership operators(in,not in)
# 20 in l1  means 20 present or not in l1
str = 'hello good morning'
print("in result : ",'good' in str) #we can find or serch char and str and case sensitive
