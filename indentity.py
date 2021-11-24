# Indetity operator
'''

a=int(input("Enter the  value of a:"))
b=int(input("Enter the  value of b:"))
print(id(a))
print(id(b))
print(a is b)

a=input("Enter the  value of a:")
b=input("Enter the  value of b:")
print(id(a))
print(id(b))
print(a is b)


a = 'python'
b = 'python'
print(id(a))
print(id(b))
print(a is b)
                   errr occured
a=input("Enter the  value of a:")
b=input("Enter the  value of b:")
print(id(a))
print(id(b))
print(a is b)


a = '4'
b = '4'
print(id(a))
print(id(b))
print(a is b)


a = input("Enter the value of a:")
b = input("Enter the value of b:")  #taking the value from the user as string
print(id(a))
print(id(b))
print(a is b)


a=[1,2,3]  #list value 
b=[1,2,3]
print(id(a))
print(id(b))
print(a is b)



a={1,2,3}  #set value
b={1,2,3}
print(id(a))
print(id(b))
print(a is b)

a = float(input("Enter the value of a:"))
b = float(input("Enter the value of b:"))
c = a
print(id(a))
print(id(b))
print(id(c))

# Operators 9
print(a is not b)
print(a is c)



a = input("Enter the value of a:")
b = input("Enter the value of b:")
c = a
print(id(a))
print(id(b))
print(id(c))

# Operators 9
print(a is not b)
print(a is c)


x=input("Enter the value of x:")
if(x is int):
 print(f"{x} is integer number")
else:
    print(f"{x} is not a interger number")

# ‘is’ operator
    
x=int(input("Enter the value of x:"))
if(type(x) is int):
    print(f"{x} is integer number")
else:                             #errorrrrrr
    print(f"{x} is not a interger number")

'''



# 'is not’ operator
        
x=int(input("Enter the value of x:"))
if(type(x) is not  int):
    print(f"{x} is integer number")
else:                             #errorrrrrr
    print(f"{x} is not a interger number")