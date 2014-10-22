#!/usr/local/bin/python3
"""Dogs and breeds"""

dogs = []

class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
      
while True:

    doggies_name = str(input("Name: "))
    if not doggies_name:
        break
    doggies_breed = str(input("Breed: "))
    dog = Dog(doggies_name,doggies_breed)
    dogs.append(dog)
    print("DOGS")
    for i in range(len(dogs)):
        print('{0}. {1}:{2}'.format(i, dogs[i].name, dogs[i].breed))
    print("*" * 40)

