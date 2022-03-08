x = int(input("please choose a number"))
y = int(input("please choose another number"))
print ("please choose a action")
print ("s = sum")
print ("d = difference")
print ("p = product")
print ("q = quotient")
print ("r = remainder")
print ("e = exponent")
operation = input("choice")
if operation == "s":
    print (" The sum of these two numbers is) " + " " + str(x+y) 
elif operation == "d": 
     absolute_value = abs(x-y)   
     print(" The difference of these two numbers is") + " " + str(absolute_value)
elif operation == "p":
    print (" The product of these two numbers is") + " " + str(x*y)
elif operation == "q":
    print (" The quotient of these two numbers is") + " " + str(x/y)
elif operation == "r":
    print (" The remainder of these two numbers is") + " " + str(x%y)
elif operation == "e":
    print (" The exponential answer of these two numbers is ") + " " + str(x**y)
else:
    print (" Not a valid operation")
