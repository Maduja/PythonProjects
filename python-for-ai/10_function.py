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