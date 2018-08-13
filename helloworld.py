# Python Tutorial Tryouts

# Print String
message = "Hello World!"
print(message.upper())

# Lists
cars = ['BMW', 'VW', 'Opel', 'Porsche']
print(cars[2].title())
print (cars[3].lower())

# String + List Value
message2 = "My first car was a " + cars[1].upper() + "."
print (message2)

# List - Last item
print "My last car was a " + cars[-1].title() + "."

# List - add item
cars.append('Bugatti')
print (cars)

# List - delete item
del cars[0]
print (cars)

# List - Pop item
popped_cars = cars.pop(2)
print (popped_cars)

# List - Remove by value
cars.remove('Opel')
print (cars)

too_expensive = 'Bugatti'
cars.remove(too_expensive)
print (cars)

# List - sorting
cars = ['BMW', 'VW', 'Opel', 'Porsche']
cars.sort(reverse=True)
print (cars)

# List - sorting temorary
print (sorted(cars))

# List - reverse the list (not alphabeticly)
cars.reverse()
print (cars)

# List - finding legnth
print (len(cars))
