#empty set
my_set = set()
print(type(my_set))

#set with values
name={"maduja","kushan","tharu","kokila"}
age=set([25,23,26,26])

print(type(name))
print(type(age))

print(age)


#adding
colors={"red","blue"}
colors.add("black")
print(colors)

#removing
colors.remove("red")
print(colors)

colors.discard("yellow")   #no error if not found
print(colors)