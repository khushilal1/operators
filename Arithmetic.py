

# Arithmetic Operators

a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
sum=a+b   #addition gives the sum of two number
print(sum)


a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
diff=a-b  #subtraction gives the differrence between two number
print(diff)


a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
product=a*b  #product gives the multipliaction of number
print(product)


a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
div1=a/b  #normal dib=vision gives the value contaning float and in value
print(div1)


a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
div2=a//b   #floored division gives the integer value of divison
print(div2)


a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
div3=a%b  #remainder division gives the remainder between two number
print(div3)

a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
pow=a**b  #exponential or power gives the value of a raised to be power b:
print(pow)

# Floor and Ceil Value in Python
import math
a=float(input("Enter the value of a:"))

# print("the ceil of 3.4 is :",end="")
# print(math.ceil(a))

print(f"The ceil of {a} is :",end="")
print(math.ceil(a))
print(f"The floor of {a} is :",end="")

print(math.floor(a))

