fruits=["banana","apple","grapes","pineapple"]

#getting items
print(fruits[3])

#slicing
print(fruits[1:])

print(fruits[0::2])

#changin an item
print(fruits)

fruits[0]="mango"
print(fruits)

#add an item
fruits.append("banana")
print(fruits)

fruits.insert(1,"kiwi")
print(fruits)

#removing
fruits.remove("banana") #remove  by value
print(fruits)

fruits.pop() #remove and return last

del fruits[0]
print(fruits)   #removing by index


#list methods

##getting information
numbers=[5,7,5,3,1,5,6,9,12,45,77,0,23]

print(len(numbers))     #length
print(numbers.count(5)) #occurrences 
print(numbers.index(5)) #find position. give first finding position

##sorting
numbers.sort()
print(numbers)      #[0, 1, 3, 5, 5, 5, 6, 7, 9, 12, 23, 45, 77]

##reverse
numbers.reverse()
print(numbers)

#copying
new_list=numbers.copy()
print(new_list)

#checking item

fruits=["banana","apple","grapes","pineapple"]
##Check if item exists
if "apple" in fruits:
    print("found")

##Check if list is empty
if fruits:
    print("list is not emplty")
else:
    print("list is empty")