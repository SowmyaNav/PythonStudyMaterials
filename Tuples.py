tup1 = (1, "Python", 2, "Java")
print(tup1)
print(type(tup1))
print(tup1[1])
print(tup1[-2])
print(tup1.count(1))
print(tup1.index("Python"))
print(tup1[0:5])

#As tuple is immutable, it throws error when executed
#tup1[0] = "Naveen"
#print(tup1)

#Converting tuple to list
l1 = list(tup1)
print(type(l1))

#Converting tuple to set
s1 = set(tup1)
print(type(s1))

#Tuple gives the length of a single string length value when one item is given in it
tup2 = ("Rathinasowmya")
print(tup2)
print(type(tup2))
print(len(tup2))
#Tuple gives the number of strings length value when more than one item is given in it
tup2 = (1, "Rathinasowmya", 2, "Chaar")
print(tup2)
print(type(tup2))
print(len(tup2))

#Tuple Unpacking
tup2 = (1, "Rathinasowmya", 2, "Chaar")
x , y, z, u = tup2
print(u)