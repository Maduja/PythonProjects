# package handling
import requests
# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

# Let's explore interactive mode
# shift+Enter
name = "Python Learner"
print(f"Hello, {name}!")

# # Some data to work with
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Calculate something
total = sum(numbers)
print(f"Total: {total}")

#operators 

result1 = 10/3
print(result1)

result2=10//3
print(result2)

result3=10%3
print(result3)

n=1_000_000
print(n)

#Single quotes
first = 'Python'

# Double quotes  
second = "Python"

#Triple quotes for multiple lines
paragraph = """This is
a multi-line
string"""

print(paragraph)