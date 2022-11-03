#just like array
# uses: handling binary data like images and exe
#value range only from 0 to 255
l = [10,20,30,40] #list
b = bytes(l) #bytes
print(type(l))
print(type(b))

print("printing bytes data :")
for x in b :
    print(x)

#range
#l1 = [10,30,50, 256] #list
#b1 = bytes(l1)  #out of range
#immutable b1[3] = 10