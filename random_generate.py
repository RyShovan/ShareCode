import random

myString = "AaBbCcDdEeFf"
type_text = ""

print(len(myString))
for i in range(50):
    type_text += myString[random.randrange(12)]

print(type_text)
