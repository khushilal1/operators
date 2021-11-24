# Logical Operators

print("HELLO   TO THE  LOGICAL OPERATOR  WORLD")
# Logical AND operator
a=int(input("Enter the value of  a:"))
b=int(input("Enter the value of  b:"))
c=int(input("Enter the value of  c:"))

if(a>0 and b>0):
    print(f"The value of {a} and {b} are grater than 0")


if(a>0 and b>0 and  c>0):
    print(f"The value of {a} ,{b} and {c} are grater than 0")
else:
    print("At least one umber ids greater  than 0")


a=int(input("Enter the value of a:"))

if(a==0 and "khushilal"):
    print("The value of a: is zero")
else:
    print("The value of a is no zero")




    # Logical OR



a=int(input("Enter the value of  a:"))
b=int(input("Enter the value of  b:"))
c=int(input("Enter the value of  c:"))

if(a>0 or b>0):
    print(f"The value of {a} or {b} are grater than 0")


if(a>0 or b>0 or  c>0):
    print(f"The value of {a} ,{b} and {c} are grater than 0")
else:
    print("At least one umber ids greater  than 0")


a=int(input("Enter the value of a:"))

if(a==0 or "khushilal"):
    print("The value of a: is zero")
else:
    print("The value of a is no zero")

  

# Logical NOT
a=int(input("Enter the value of a:"))
if not a==a:
    print(f"{a} is not equal to {a}")
else:
    print(f"{a} is equal to {a}")
