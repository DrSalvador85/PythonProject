import random

numberListOne = []
numberListTwo = []
for i in range(1,10):
     numberListOne.append(random.randint(1,10))
for j in range(1,10):
     numberListTwo.append(random.randint(1,10))

print(f"The first list to be automatically created was {numberListOne}")
print(f"The Second list to be automatically created was {numberListTwo}")

common = [];
for  isThere in numberListOne:
     if   isThere in numberListTwo:
          common.append(isThere)     
print(f"The common components were {common}")