# it is read only version of LIST
#order is followed
#() used for tuple
a = ('viny',10,20,30)
print(type(a))
print("tuple is :",a)
print("first and last elemt of tuple is: ",a[0],a[-1])

# not possible to aappend or remove element from tuple 
#immutable cant change
# a[0] = 77 #type error
# print(a)

#EMPTY tuple
a1 = ()
print("empty tuple result : ")
print(type(a1))

#tuple with one value is NOT tuple
a2 = (10)
print(type(a2)) #this is int
a3 = ('vinay')
print(type(a3)) #this is str
a4 = (10,)
print(type(a4)) # this is tuple

#why this issue is because in normal maths we represent 10 also as (10) so for tuple it should be (10,)
#helpful in condition where we have only few condition or fixed condition ex: atm saving and current


