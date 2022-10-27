# list is order specific and duplicate allowed
l = [10,'vinay',20,10,30]
print(type(l))
print(l)    
#print as it is because list follow order of input given
# and must be used [] 
# and can multiple datatypes
print(l[0])
print(l[-1])
print(l[1:4]) #list of elements from 1 to 4-1 print 3 words

#inserting and removing elements
print("append output:")
a = []  #empty list
a.append('vinay')
a.append(40)
a.append(20)
a.append(10)
a.append(40)
print(a)
a.remove(40)  # it will remove only first occurence of 40
print(a)

#replacing elements in list
a[0]=77
print(a) #mutable so we can change value anytime