list1 = [10 , 20]
print(list1)
print(type(list1))
list2 = ["Sowmi", 1829, 23, 234.54, True, 23]
print(list2)
print(len(list2))
print(list2[-1])
print(list2.count(23))
list2[0] =50
print(list2)
#append
list2.append(18)
print(list2)
#Add a list into another list
list1 = [10, 43, 75, 20, 30]
list2 = ["sow", "nav", "chaar"]
list3 = "Python"
list1.extend(list2)
print(list1)
list1.extend(list3)
print(list1)
#Pop
list1.pop(1)
print(list1)
#Remove
list2.remove("sow")
print(list2)
#Sort
list1 = [10, 43, 75, 20, 30]
list1.sort()
print(list1)
#Reverse
list1.reverse()
print(list1)




