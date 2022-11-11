#logical operators
#and or not
# and if both are true then true
# or if one is true then true
# not if true then false and false then true
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(not True)
print(not False)

# logical op for non-boolean 
# x and y  o/p will be also non boolean if they non boolean true and y so x value
# x is false in case boolean then false (x is enough to decide) 
# x is true in case boolean then false (depends on y)


print("printing non - boolean and : ")
# x and y o/p will be non boolean if both are non boolean 
# x evaluates to true, then result is y
# x evaluates to false then result is x
print(10 and 20)
print(0 and 20)

# x or y o/p will be non boolean if both are non boolean 
# x evaluates to true, then result is x
# x evaluates to false then result is y
print(10 or 20)
print(0 or 20)

print("not oper data : ")
print(not 10)
print(not 0)
