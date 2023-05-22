fname = "Sowmi"
lname = "Chaarvi"
print(fname)
print(lname)
print(fname+lname)
print(fname+ " " +lname)
#Indexing & Built-in methods
sent =" i love python"
print(sent)
print(len(sent))
print(sent.index('p'))
print(sent.replace('p','r'))
print(sent.split('p'))
print(sent.upper())
print(sent.lower())
print(sent.title())
print(sent.islower())
print(sent.isupper())
print(sent.count('o'))

name= "sowmi"
print("I like "+name)
#Format Method
myLang = "I know {}".format("Java")
print(myLang)
#Format Method with index
myLang = "I know {1} {2} {0}".format("Java", "Python", "JS")
print(myLang)

#f String
name= "Sowmi"
prog= "Python"
print(f"My name is {name} and I know {prog}")

#Slicing
sent = "Python is very easy"
print(sent)
print(sent[6])
print(sent[-1])
print(sent[2:])
print(sent[2:6])
print(sent[::2])
print(sent[::-1])
