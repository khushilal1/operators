# Membership Operators

a=[1,2,3]
print(a in a)  #in opertaor check the value in the given list

a=[1,2,3]
print(2 in a)

a=[1,"string",3]
print("string" in a)

a=(1,2,3,4)
print(2 in a)


a=[1,2,3,4,5]
b=[1,2,3,4,5]

for item in a:
  print(item)
  if item in b:
    print("overlapping both a and b")
  else:
      print("Not ovrlapping")



      
a=[1,2,3,4,5]
b=[1,2,3,4,9]

for item in a:
  print(item)
  if item in b:
    print("overlapping both a and b")
  else:
      print("Not ovrlapping")


# ‘not in’ operator-


a=[1,2,3]
print(1 not in a)  #in opertaor check the value in the given list

a=[1,2,3]
print(2 in a)



      
a=[1,2,3,4,5]
b=[1,2,3,4,9]

for item in a:
  print(item)
  if item not in b:
    print("overlapping both a and b")
  else:
      print("Not ovrlapping")


