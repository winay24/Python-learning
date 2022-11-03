#bytes is mutable and bytesarray is mutable
#just because of immutability for bytes we have bytearray
l=[20,30,40,50]
ba = bytearray(l)
print(type(ba))
print(ba[0])
print(ba[1])
ba[2] = 255
print(ba[2])