#none means nothing so no value associated
#use case 1:
a = 10
a = None  #which will deallocate memory of a

print(a)  # None
print(type(a)) #Nonetype
print(id(a)) #address of a

#use case 2:
#in some cases no value for variable that will be allocated by None value

def f1():
    return 10

x = f1()
print(x) #print 10 but if no return statement there then it will assign by None value
