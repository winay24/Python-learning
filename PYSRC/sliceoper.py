#slice operator s[begin:end]
s = "vinay kumar reddy"
print(s[0:10]) #helpful to print only specific part of string
print(s[ : ]) #begin to end
print(s[5:1]) #empty

#USES
s1 = 'vinay reddy'
print(s1[0].upper()+s1[1:])  #will print first letter caps and remaining as it is
#not only starting anywhere we want
print(s1[-1])  #will print last letter of that string


#about string
a = '''vinay
        kumar
            reddy'''    #''' helpful to print exact pattern
print(a)

a1 = "vinay 'reddy'"
print(a1)  #we can print ' but we have to use in "
a2 = 'vinay "reddy"'
print(a2)

#about variable naming
#shouldn't start with number and no special character or no reverse words 
#case sensitives

# about + , * operator with string
b1 = 'vinay '
b2 = 'kumar '
c = b1 + b2
print(c)
c1 = b1*3
print(c1)
