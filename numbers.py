#for loop for listing values vertically
for values in range(1,21):
	print(values)

#using range() function within the list() function
numbers = list(range(1,21))
print(numbers)

#same as above, except starting is 2, then the last argument just adds by that amount each time
even_numbers = list(range(2,41,2))
print(even_numbers)

#same as above, except starting at 1
odd_numbers = list(range(1,41,2))
print(odd_numbers)


