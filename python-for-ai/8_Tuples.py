#empty tuple
my_tuple=()

#tuple with items
point=(3,5,7,4,8,1,4,5)

#single item tuple
single1=(43,)
single2=(43)

print(type(single1))
print(type(single2))

coordinates = 10, 20
print(type(coordinates))

#accessing
print(point[3])

#Tuple unpacking
number=(3,5)
x,y = number
print(x)
print(y)