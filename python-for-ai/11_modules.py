# import math

# print(math.sqrt(16))


from math import sqrt
print(sqrt(16))

import random
number= random.randint(1,7)
print(number)

fruit = random.choice(["banana","apple","pineapple"])
print(fruit)

# Date and time
import datetime
to = datetime.date.today()
print(to)

# Operating system
import os
current = os.getcwd()
print(current)

#json
import json
data = {"name":"maduja","age":25}
json_string=json.dumps(data)
print(json_string)

# Import with alias
import pandas as pd
df = pd.DataFrame(data)