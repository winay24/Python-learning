# same as set except immutable (we cant modify it is immuutable)
s = {1,2,3,4,'vinay'}   #this is set
fs = frozenset(s)  #this is frozen set
s1 = {1,2,1} #1 only one time
print(type(fs))

print("testing : ")
#fs.add(10)   #add or remove not poaasible for frozen set
#fs[0]   #no order followed so not possible

#difference b/w tuple and frozenset
#order not follwed in fs and duplicates not allowed and index , slice also not applicable