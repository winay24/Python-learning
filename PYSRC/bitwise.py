# bitwise operators :  &(and)  |(or)  ^(x-or)  ~(compliment)  <<(left)  >>(right shift)
#for only int and bool type

#&  and
#1 & 1 = 1
#-----------------------
#| or
# 0 | 0 = 0
#
# -------------
#exor ^
#  1 ^ 0 = 1 , 0 ^ 1 = 1

print("& : ",4 & 5)
print("| : ",4 | 5)
print("^ : ",4 ^ 5)

#------------------------
# ~ 0 to 1 and 1's to 0's
print("~ : ",~4) # -(a+1) because 32bits 
print("~ : ",~10)
print("~ : ",~-10)
# 1's compliment  1->0 , 0->1
# 2's comppliment 1's-compliment + 1

#--------------------------shift operators
# left and right 
# 10<<2 = 40 ; 10* 2power2 =40; 10 in binary 1010 => 2times left == 101000 == 40 left means 0 at end
# 10>>2 =    ;  10/2poer2 = 2 ' 10 == 0000....1010  ==> 000000..... 10  == right depends on sign bit
#-----------------------------------------------------------------------------------boolean with bitwise
print("printing boolean data : ")
print(True & False)
print(True | False)
print(True ^ False)
print(~False)
print(True << False)
print(True >> False)