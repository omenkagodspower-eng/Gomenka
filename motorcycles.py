motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#modifying elements in a list
motorcycles[0] = 'ducatti'
print(motorcycles)

#adding new element to a list using append
motorcycles = ['honda', 'yamah', 'suzuki']
print(motorcycles)

motorcycles.append('ducatti')
print(motorcycles)  

#using append by starting with an empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducatti')
print(motorcycles)

#inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducatti')
print(motorcycles)

#Removing an item using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

#Removing an item using the pop method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)    

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle i owned was a " + last_owned.title() + "." )

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle i owned was a ' + first_owned.title() + ".")

#Removing an item by value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)