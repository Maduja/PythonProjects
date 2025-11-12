class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

dog1 = Dog("Buddy","Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Or with named arguments (clearer)
dog3 = Dog(name="Charlie", breed="Poodle")

print(dog1.name)
print(dog2.breed)

dog1.name="Rexy"
print(dog1.name)

"""When defining methods in a class, you always include self 
as the first parameter. But when calling the method, you 
don’t pass it - Python does that automatically!
"""

#---------------------------------------------------------------------

class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000


#-----------------------------------------------------------------
class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']


#------------------------------------
class Dog:
    def __init__(self,name):
        self.name=name

    def bark(self):
        print("bark")

dog1=Dog("Brownie")

dog1.name
dog1.bark

