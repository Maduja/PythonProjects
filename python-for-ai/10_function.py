def greet():
    print("hello World!")
    print("Welcome to python!")

greet()
greet()


def check_temparature():
    temp=25
    if temp>=25:
        print("hot")
    else:
        print("cold")

check_temparature()



#functions with parameters
def greeting(name):
    print(f"Hello {name}")


greeting("maduja")

#multiple parameters with default values
def student_info(name,age,uni="UWU"):
    print(f"Student name is {name},and age is {age} and uni is {uni}")


student_info("maduja",25)


def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)



def sum(a,b):
    print(a+b)

sum(12,34)


#return
def sum_return(a,b):
    return a+b


total=sum_return(3,2)
print(total)

print(f"total is {sum_return(3,6)}")


#multiple return
def get_min_max(numbers):
    return min(numbers), max(numbers)


minimum,maximum = get_min_max([3,5,6,4,2,1,6,9,1])
print(minimum)
print(maximum)