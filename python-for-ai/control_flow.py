temperature = 25

if temperature > 30:
    print("It's hot!")
else:
    print("Nice weather!")


score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")


#nested if
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")

#multiple conditions
age = 25
has_license = True

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")




for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(1,6,2):
    print(i)

name="python"
for i in name:
    print(i)

colors=["red","white","black"]
for i in colors:
    print(f"i like {i}")

count=0
while count<5:
    print(count)
    count+=1