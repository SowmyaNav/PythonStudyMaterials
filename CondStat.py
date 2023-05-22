# if Statement
print("Welcome")
a = 10
if a>50:
    print("Hello")
print("Thanks")

# if...else Statement
print("Welcome")
a = 80
if a>500:
    print("Hello")
else:
    print("Not applicable")
print("Thanks")


name = "Python"
if name == "Python":
    print("Python Found")
else:
    print("Python not Found")
print("Thanks")

#elif
lang = "Python"
if lang == "Selenium":
    print("Selenium found")
elif lang == "Python":
        print("Python found")
elif lang == "Java":
        print("Java found")
else:
    print("Not found")


#elif input got from user
lang = input("Please enter the programming language:")
if lang == "Selenium":
    print("Selenium found")
elif lang == "Python":
        print("Python found")
elif lang == "Java":
        print("Java found")
else:
    print("Not found")