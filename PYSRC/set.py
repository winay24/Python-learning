# duplicates are not allowed and order not important
#{} used to represent

s = {10,20,30}
print(type(s))

s1 = {10,20,'vinay',30,'vinay'}
print(type(s1))
print(s1)  #ignores duplicates print only once and won't follow order
#print(s1[0]) this will through error because order not followed even slice oper not allowed for set

#adding elements from set
s1.add(40) #append for list and add for set
print(s1)
s1.remove(20)
print(s1)  #mutable we can do changes like list

#reason for not append because append means adding at end so in set we can't add end not sure

#empty set there is no empty set we call it as dict because of priority od dict this exist
s2 = {}
print(type(s2)) #will give as dict

#how to create empty set
s3 = set()
print(type(s3))  # as set
print(s3) #empty set 