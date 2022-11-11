#equality operators
print(10 == 20)
print(1 == True)
print(0 != True)
print(1 != True)
print("vinay" == "vinay")
print(10 == "durga")  # == gives False o/p not error
print(10 == "10")

#difference b/w ==  and is
# a is b   is true when both refered to same object
# a == b   is true when a and b have same content
l1 = [10,20,30]
l2 = [10,20,30]
print("id of l1",id(l1))
print("id of l2",id(l2))
print("printing is o/p",l1 is l2) # address is different so FALSE
print("printing == o/p", l1 == l2) # contnet same so TRUE
l3 = l1
print("printing l1 is l3 o/p",l1 is l3) # pointing to same so TRUE