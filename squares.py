#Create an empty list because we're using a for loop to not only create the values in the range, but also because the loop will square each of those values in the range
squares = []
for value in range(1,21):
	square = value**2
	squares.append(square)
	
print(squares)


#But wait we don't even need the 'square' variable lol...
squares2 = []
for value2 in range(1,21):
	squares2.append(value2**2)
print(squares2)

#BUT WAIT, there's more... we can use list comprehension and drop down to 1 line:
square3 = [value**2 for value in range(1,21)]
print(square3)

#Lets do some statistics
#digits = list(range(0,6))
#print(digits)
#print(min(digits))
#print(max(digits))
#print(sum(digits))

squares4 = [value4**2 for value4 in range(2,200)]
print(squares4)
