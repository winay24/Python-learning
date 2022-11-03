#most commonly used datatype
#FORM-1 with default start from0 and one argument
r = range(10)    #0 to 9
print(type(r))

#print(r) #it won't print range
#it will print 0 to 9
for x in r :
    print(x)

#FORM-2   two arguments
#r = range(begin,end)
r1 = range(1,10)  #1 to 9
print("printing range from 1")
for x in r1 :
    print(x)

#FORM-3  WITH 3 ARGUMENTS
#r = range(begin,end,increment)
#increment
r2 = range(10,100,3)
print("printing form-3")
for x in r2 :
    print(x)

print("testing")
r3=range(-10,10,1)
for x in r3 :
    print(x)

#decrement
print("test of decrement")
r4 = range(29,0,-1)
for x in r4 :
    print(x)

print("printing index and slice: ")
print(r4[-1])
print(r4[0])
r5 = r4[0:5]
for x in r5 :
    print(x)

#immutable can't change value because it effect order of value