emp = {"QA": "Sowmi", "Dev": "Nav" , "DevOps": "Madhan"}
print(emp)
print(emp["QA"])
print(emp.get("Dev"))

#List concept in Dictionary
emp = {"QA": ["A", "B", "C"], "Dev" : "D", "Devops": "E"}
print(emp["QA"][1])
print(emp["QA"])
#Returns all keys
print(emp.keys())
#Returns all values
print(emp.values())
#Returns all keys+values
print(emp.items())
del emp
