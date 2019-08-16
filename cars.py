#Sorting lists. We usually have random lists, but we can use sort() method to have some sort of structure
cars = ['bmw', 'audi', 'toyota', 'nissan']
print(cars)
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'nissan']
print(cars)

#Reverse sort!
cars.sort(reverse=True)
print(cars)

#This does the same as the sort() METHOD. But, does NOT change it permanently. 
#sort() is a method, while sorted() is a FUNCTION
print(sorted(cars))


print("Here's the original list of inputs:\n" + str(cars))
print("Here's the sorted list of inputs:\n" + str(sorted(cars)))


#Extra:
zain = ['c', 'C', 'a']
print(zain)
zain.sort()
print(zain)
zain.sort(reverse=True)
print(zain)
print(zain)

#Also can reverse, but not alphabetically. Just reverse from original list. 
print('Reverse')
print(zain)
zain.reverse()
print(zain)
zain.reverse()
print(zain)
print("Length:")
print(len(zain))
