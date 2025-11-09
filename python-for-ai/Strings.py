#String concatenation 
first_name = "maduja"
second_name = "verjini"
full_name = first_name + " " + second_name
print(full_name)

#string repetetion 
star='*'
print(star*5)

#length
message="Maduja verjini abhayasundara is a computer science undergraduate at Uva wellassa university"
print(len(message))

empty=" "
print(len(empty))

#converting to string
age=25
msg="my age is "
print(msg + str(age))

name="maduja"
uni = "UWU"
print(f"My name is {name} and my university is {uni}")

#string methods
name = "               maduja verjini"
print(name.lower())
print(name.upper())
print(name.title())
print(name.strip())

#finding 
text = "I love Python programming with Python"
print("Python" in text)
print(text.startswith("l"))
print(text.startswith("I"))
print(text.endswith("n"))

print(text.find("love"))
print(text.count("Python"))

new_msg = text.replace("Python","Java")
print(new_msg)