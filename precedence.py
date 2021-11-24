# Operator Precedence
'''
a=10+23*2  #predece of multipliaction of subtractiun grrater thanadd so firstly addition is done
print(a)  #precedence of add and multiplication

a=(10+2)*3  #addition isdone first because addition is under the parenthesisia
print(a)  #predecnce of parenthesisi and multipliaction


a="john"
b=24
if(a=="john" or a=="mohan" and b==34):
    print("hello khushilal")
else:
    print("not mathch")


    # Operator Associativity
a=float(input("Enter tthe value of a:"))
b=float(input("Enter tthe value of b:"))
c=float(input("Enter tthe value of c:"))
print(a/ b *c)  #precendece of all m opertaor are same but exction if from lrft to right


a=float(input("Enter tthe value of a:"))
b=float(input("Enter tthe value of b:"))
c=float(input("Enter tthe value of c:"))
print(a* b /c)  #precendece of all m opertaor are same but exction if from lrft to right




a=float(input("Enter tthe value of a:"))
b=float(input("Enter tthe value of b:"))
c=float(input("Enter tthe value of c:"))
print(a ** b ** c)


a=float(input("Enter tthe value of a:"))
b=float(input("Enter tthe value of b:"))
c=float(input("Enter tthe value of c:"))
print((a ** b) ** c)




# Difference between == and is operator
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(id(a))
print(id(b))

if(a==b):
    print(f"Both {a} and {b} are equal")
else:
    print(f"Both {a} and {b} are not equal")



a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(id(a))
print(id(b))
if(a is b):
    print(f"Both {a} and {b} are equal")
else:
    print(f"Both {a} and {b} are not equal")


a=[1,2,3,4]
b=[4,5,6,7]
c=a+b
print(c)
    '''

# c=a-b  #invalid method for (-)
# print(c)

# a={1,2,3,4}
# b={4,5,6,7}  #set caanot be concatetening
# c=a+b
# print(c)


a=(1,2,3,4)
b=(4,5,6,7)
c=a+b
print(c)


