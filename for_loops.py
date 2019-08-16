#List of something
magicians = ['Dumbledore', 'Voldemort', 'Merlin']
#for loop for all values in the list, to be displayed
#indentation is needed for any code within the for loop
#colon indicates start of loop
for magician in magicians:
	print(magician.title() + ", an excellent sorcerer.")
	print("Looking forward to seeing you grow, " + magician + ".\n")

#This is different. It will print globally, rather than iterated throughout the loop
print ("Thank you all for coming.")
