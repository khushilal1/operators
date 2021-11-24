
# Short Circuiting
x = float(input("Enter the value of x:"))
y = float(input("Enter the value of y:"))
print(x >= 2 or (x/y) > 2)


x = float(input("Enter the value of x:"))
y = float(input("Enter the value of y:"))
print(x >= 2 and (x/y) > 2)



print(x >= 2 and (x/y) > 2)
print(x >= 2 and y != 0 and (x/y) > 2)
print((x >= 2 and y != 0 and (x/y) > 2))