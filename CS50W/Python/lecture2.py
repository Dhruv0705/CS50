#       Formatting Strings

name = str(input("Name: "))
print(f"Hello, {name}")

print("_____________________")

#       Conditions


n = int(input("Number: "))
if n>0:
    print(n, "is positive")
elif n<0:
    print(n, "is negative")
else:
    print(n, " is equal to n")

print("_____________________")

#       Sequence

name1= "Dhruv"
print (name1[0])
#List [sequence of mutable values]
nameList = ["Dhruv", "Jay"]
print (nameList[1])

nameList.append("Fin")
nameList.sort()
print(nameList)

#Tuple (sequence of immutable values)
coordinateX=10.0
confidanteY=20.0
confidante = (10.0,20.0)

#Set
s= set()
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(4)
print(s)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements.")

print("_____________________")

#       Loops

for i in [0,1,2,3]:
    print(i)
print("_____________________")
for i in range(4):
    print(i)
print("_____________________")
for i in nameList:
    print(i)
print("_____________________")
for i in name1:
    print(i)
print("_____________________")

#       Dictionaries

houses={"Harry": "Gryffindor", "Draco": "Slytherin"}
houses["Hermione"] = "Gryffindor"
print(houses["Harry"])
print(houses["Hermione"])
print("_____________________")

#       Functions

def square(x):
    return x * x 

for i in range(6):
    print(f"The square of {i} is {square(i)} ")

print("_____________________")
#     Import Options
#from (file name) import (function)
#       OR
# import (filename) 
# call function (filename).(function) 

#       Object-Oriented (Class)

class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
    
p=Point(2,8)
print(p.x)
print(p.y)

print("_____________________")

# Adding person to flight  

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers= []

    def add_passenger(self, passenger_name):
        if not self.open_seat():
            return False
        self.passengers.append(passenger_name)
        return True

    def open_seat(self):
        return self.capacity- len(self.passengers)

flight=Flight(3)

people= ["Dom", "Daniel", "Tom", "Fin"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully ")
    else:
        print(f"No available seats for {person}")

print("_____________________")
#       Functional Programming
# Decorators

def announce(f):
    def wrapper():
        print("About to run the function....")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello World!!")

hello()

print("_____________________")

# Lambda

people1= [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people1.sort(key=lambda person: person["name"])

print(people1)

print("_____________________")

import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try: 
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")