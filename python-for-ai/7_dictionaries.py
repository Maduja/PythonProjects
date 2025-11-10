#creating empty dictionary
my_dict ={}

#dictionary with data
person = {
    "name":"maduja",
    "age":25,
    "city": "colombo"
}

print(person)

#another way of creating dictionary
scores = dict(math=95, science=76, english=98)
print(scores)

#Accessing values

print(person["name"])
print(person["age"])

#safer with get()
print(person.get("job"))
print(person.get("job","unknown"))

#add or update
person["email"]="madujav@gmail.com"
print(person)

person["age"]=26
print(person)

#update multiple keys
person.update({"age":30, "email":"mv@gmail.com"})
print(person)

#removing
del person["city"]      #remove by key
person.pop("age")       #remove and return
person.clear()          #remove all items

print(person)

#Dictionary methods
student = dict(name="maduja",age=25,subject="OOP")
print(student)

print(type(student))

print(student.keys())
print(student.values())
print(student.items())

# Check if key exists
if "name" in student:
    print("found")

#check dictionary empty or not
student.clear()

if student:
    print("not empty")
else:
    print("empty")

#nested dictionary

store={
    "book":{"name":"8 rules of love","author":"jay shetty"},
    "stationary":{"pen":["red","black","blue"], "wBook":["CR","A4","B5"]}
}

print(store)
print(type(store))
#accessing
print(store["book"]["author"])